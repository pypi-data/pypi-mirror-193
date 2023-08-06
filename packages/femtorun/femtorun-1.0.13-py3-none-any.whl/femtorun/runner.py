"""Define the runtime interface"""
import numpy as np
from collections import defaultdict
import textwrap
import copy
import re

import time

import logging
logger = logging.getLogger(__name__)

from typing import *
import numpy.typing as npt
NDARRAYINT = npt.NDArray[int]
NDARRAYINT64 = npt.NDArray[np.uint64]
VARVALS = Dict[str, NDARRAYINT]

class FemtoRunner:
    """Supports input/output padding for all derived runtimes

    Derived runners might pad inputs and outputs internally

    Args:
        input_padding (dict {varname : (logical len, padded len)}, or None):
            Padding description for inputs; None for no padding
        output_padding (dict {varname : (logical len, padded len)}, or None):
            Padding description for outputs; None for no padding
    """
    def __init__(self, input_padding, output_padding):
        self.input_padding = input_padding
        self.output_padding = output_padding

        def check_padspec(padding):
            for _, pad_spec in padding.items():
                if len(pad_spec) > 2:
                    raise NotImplementedError(
                        'inputs and outputs greater than 2D (for a timestep) not supported')

        if self.input_padding is not None:
            check_padspec(self.input_padding)
        if self.output_padding is not None:
            check_padspec(self.output_padding)

    def reset(self, reset_vals=None):
        """Reset (or initialize) the runner

        Typically used for bookkeeping values
        """
        raise NotImplementedError("Derived class of FemtoRunner must implement")

    def finish(self):
        raise NotImplementedError("Derived class of FemtoRunner must implement")

    def set_vars(self, set_vals):
        raise NotImplementedError("Derived class of FemtoRunner must implement")

    def get_vars(self, varnames):
        raise NotImplementedError("Derived class of FemtoRunner must implement")

    def _pad_inputs(self, input_vals : VARVALS) -> VARVALS:
        if self.input_padding is None:
            return input_vals
        else:
            # pad zeros
            padded = {varname : np.zeros(padshape, dtype=int)
                        for varname, (logicalshape, padshape) in self.input_padding.items()}

            for varname, (logicalshape, padshape) in self.input_padding.items():
                varshape = input_vals[varname].shape
                if len(varshape) == 1:
                    padded[varname][:varshape[0]] = input_vals[varname]
                elif len(varshape) == 2:
                    padded[varname][:varshape[0], :varshape[1]] = input_vals[varname]
                else:
                    assert False
            return padded

    def _unpad_outputs(self, output_vals : VARVALS) -> VARVALS:
        if self.input_padding is None:
            ret = output_vals
        else:
            unpadded = {}
            for varname, (logicalshape, padshape) in self.output_padding.items():
                if len(padshape) == 1:
                    unpadded[varname] = np.atleast_1d(output_vals[varname])[:logicalshape[0]]
                elif len(padshape) == 2:
                    unpadded[varname] = np.atleast_2d(output_vals[varname])[:logicalshape[0], :logicalshape[1]]
                else:
                    assert False
            ret = unpadded
        return ret

    def step(self, input_vals):
        """Execute one timestep, driving input_vals and getting outputs

        Args:
            input_vals (dict {varname (str): val (numpy.ndarray)):
                Variable names and their values for one timestep

        Returns:
            (output_vals, internal_vals) tuple(dict, dict)):
                tuple of dictionaries with same format as input_vals,
                Output variables and their values, and
                internal variables and their values
        """
        raise NotImplementedError("Derived class of FemtoRunner must implement")

    def run(self, input_val_timeseries):
        """Execute several timesteps, iterating through the values of input_val_timeseries
        driving the runner at each timestep. Calls .step() each timestep.

        Args:
            input_val_timeseries (dict {varname (str): value (numpy.ndarray)}):
                keyed by variable names, values are numpy arrays, first dim is time

        Returns:
            (output_vals, internal_vals, output_valid_mask) tuple(dict, dict, dict)):
                tuple of dictionaries with same format as input_vals,
                values for the output variables as well as all internal variables,
                for all timesteps that were run
                output_valid_mask contains a 1D bool array for each key, says whether each output
                was produced on a given timestep
        """

        # check that indexables are all the same length
        first_var_vals = next(iter(input_val_timeseries.values()))
        n_steps = first_var_vals.shape[0]
        if not all(val.shape[0] == n_steps for val in input_val_timeseries.values()):
            raise ValueError("Input sequence lengths don't match for all variables")

        # run simulation, calling step, building up lists for outputs and internal states
        output_vals = {}
        output_valid_mask = {}
        internal_vals = {}

        for i in range(n_steps):
            step_inputs = {varname: values[i] for varname, values in input_val_timeseries.items()}

            step_out, step_internals = self.step(step_inputs)

            for varname, val in step_out.items():
                if varname not in output_vals:
                    output_vals[varname] = np.zeros((n_steps, *val.shape), dtype=val.dtype)
                    output_valid_mask[varname] = np.zeros(n_steps, dtype=bool)
                output_vals[varname][i] = val
                output_valid_mask[varname][i] = True

            for varname, val in step_internals.items():
                if varname not in internal_vals:
                    assert i == 0, "should have all internal values, every step"
                    internal_vals[varname] = np.zeros((n_steps, *val.shape), dtype=val.dtype)
                internal_vals[varname][i] = val

        FemtoRunner.check_mask_complete(output_valid_mask) # XXX for now

        return output_vals, internal_vals, output_valid_mask

    @classmethod
    def compare_outputs(cls, name_A : str, output_A : VARVALS, name_B : str, output_B : VARVALS, error_tolerance : Union[None, float, int]=None):

        shape_dict = lambda x : {k : v.shape for k, v in x.items()}
        contents_str = (f"compare_outputs() : {name_A} vs {name_B} :\n"
                    f"{name_A} shapes :\n" +
                    f"{textwrap.indent(str(shape_dict(output_A)), '  ')}\n" +
                    f"{name_B} shapes :\n" +
                    f"{textwrap.indent(str(shape_dict(output_B)), '  ')}\n")

        key_err_str = ""
        for k in sorted(set(output_A.keys()) | set(output_B.keys()), key=cls._sortkey):
            key_err_str += f"{k} :\n"
            if k in output_A:
                key_err_str += f"  {name_A} had:\n"
                key_err_str += f"{textwrap.indent(str(output_A[k]), '    ')}\n"
            else:
                key_err_str += f"  MISSING FROM {name_A}!:\n"

            if k in output_B:
                key_err_str += f"  {name_B} had:\n"
                key_err_str += f"{textwrap.indent(str(output_B[k]), '    ')}\n"
            else:
                key_err_str += f"  MISSING FROM {name_B}!:\n"

        # check that both return the same variables
        if set(output_A.keys()) != set(output_B.keys()):
            logger.debug(contents_str)
            logger.debug(key_err_str)
            logger.error(f"mismatch between {name_A} and {name_B}s' keys\n" +
                    f"{name_A} had {output_A.keys()}\n"
                    f"{name_B} had {output_B.keys()}\n"
                    "the runners are returning different variables\n")
            return -1

        # check some types, shapes
        had_shape_error = False
        non_matching_shapes = ''
        for k, v_A in output_A.items():
            v_B = output_B[k]
            assert isinstance(v_B, np.ndarray) # something's really wrong if this happens
            assert isinstance(v_A, np.ndarray) # something's really wrong if this happens
            if v_A.shape != v_B.shape:
                had_shape_error = True
                non_matching_shapes += f'{k} : {name_A} had {v_A.shape} vs {name_B} had {v_B.shape}\n'

        if had_shape_error:
            errstr = ("variable names matched, but returned values' shapes didn't\n" + non_matching_shapes)
            logger.debug(contents_str)
            logger.debug(key_err_str)
            logger.error(errstr)
            return -1

        # now check all values
        bad_keys = []
        for k, v_A in output_A.items():
            v_B = output_B[k]
            if error_tolerance is None:
                if not np.all(v_A == v_B):
                    bad_keys.append(k)
            else:
                if not np.all(np.abs(v_A - v_B) <= error_tolerance):
                    bad_keys.append(k)

        if len(bad_keys) > 0:
            errstr = ("variable names matched and returned values' shapes matched, but values are wrong\n" +
                    "these keys had mismatches:\n")
            for k in bad_keys:
                errstr += f"{k} :\n"

            errstr += "these were the mismatches:\n"

            for k in bad_keys:
                errstr += f"{k} :\n"
                errstr += f"{name_A} had:\n"
                errstr += f"{textwrap.indent(str(output_A[k]), '  ')}\n"
                errstr += f"{name_B} had:\n"
                errstr += f"{textwrap.indent(str(output_B[k]), '  ')}\n"
                errstr += f"difference ({name_A} - {name_B}):\n"
                errstr += f"{textwrap.indent(str(output_A[k] - output_B[k]), '  ')}\n"

            logger.debug(contents_str)
            logger.debug(key_err_str)
            logger.error(errstr)
            return -1
        else:
            logger.debug("ALL INTERNAL COMPARISONS OK!")
        return 0

    @classmethod
    def _sortkey(cls, x):
        endnum = re.search(r'\d+$', x)
        if endnum:
            return int(endnum.group())
        else:
            return 0 # others wind up in random order

    @classmethod
    def compare_internals(cls, name_A : str, output_A : VARVALS, name_B : str, output_B : VARVALS, error_tolerance : Union[None, float, int]=None):
        """more lax than compare outputs, not all variables need to be the same
        due to optimization, expansion, etc, they keys in each output won't match generally.
        Matched keys are assumed to be key points, and are compared
        """
        # usual variable names from fqir are %x.NNN
        # normal sort puts %x.13 before %x.9, e.g.

        key_points = sorted(output_A.keys() & output_B.keys(), key=cls._sortkey)
        key_A = {k : output_A[k] for k in key_points}
        key_B = {k : output_B[k] for k in key_points}
        missing_A = sorted(output_A.keys() - key_points, key=cls._sortkey)
        missing_B = sorted(output_B.keys() - key_points, key=cls._sortkey)

        logger.debug("Comparing Internal Values")
        logger.debug("Key Points:")
        logger.debug("%s", str(key_points))
        logger.debug("%s had these variables, %s didn't. NOT COMPARED:", name_A, name_B)
        logger.debug("%s", str(missing_A))
        logger.debug("%s had these variables, %s didn't. NOT COMPARED:", name_B, name_A)
        logger.debug("%s", str(missing_B))

        cls.compare_outputs(name_A, key_A, name_B, key_B, error_tolerance)

    @classmethod
    def check_mask_complete(cls, mask):
        """for now, we don't handle checking outputs that don't have full masks
        this functionality can be added later and this check removed"""
        for k, v in mask.items():
            if np.sum(v.flatten()) != np.product(v.shape):
                raise NotImplementedError()

    @classmethod
    def compare_runs(cls, inputs : VARVALS, *runners, names : Union[None, List[str]]=None, compare_internals=False, except_on_error=True, error_tolerance : Union[None, float, int]=None):
        """run two FemtoRunners next to each other and compare the outputs

        doesn't compare internal states, which can be hard to generalize, returns them instead

        Args:
            inputs : (dict) : same format to FemtoRunne.run()
            *runners : (variable number of :obj:`FemtoRunner`) : the FemtoRunners to compare
            compare_internals : also check internal variables values' match
        """
        np.set_printoptions(threshold=10000)

        if names is None:
            names = [runner.__class__.__name__ for runner in runners]
        assert len(names) == len(runners)

        outs = []
        internals = []
        out_masks = []
        durs = []

        def run_one(name, runner):
            t0 = time.time()

            try:
                runner.reset()

                out, internal, out_mask = runner.run(inputs)
                outs.append(out)
                internals.append(internal)
                out_masks.append(out_mask)

                runner.finish()
            except:
                runner.finish() # we need to try to exit cleanly for some runners, notably FB's SimRunner
                raise

            tdur = time.time() - t0
            durs.append(tdur)

        for name, runner in zip(names, runners):
            run_one(name, runner)

        saw_err = False
        for name, runner, out in zip(names[1:], runners[1:], outs[1:]):
            err = FemtoRunner.compare_outputs(names[0], outs[0],
                                              name,     out, 
                                              error_tolerance)
            saw_err = saw_err or (err != 0)

            if err:
                # if the output didn't match, run the internal comparison anyway for debug purposes
                logger.info("Output comparison failed! checking internal key points (if supplied)")
                for name, runner, out in zip(names[1:], runners[1:], internals[1:]):
                    FemtoRunner.compare_internals(names[0], internals[0],
                                                  name,     out, 
                                                  error_tolerance)

        if compare_internals:
            # check internal values that name-match
            for name, runner, out in zip(names[1:], runners[1:], internals[1:]):
                err = FemtoRunner.compare_internals(names[0], internals[0],
                                                    name,     out, 
                                                    error_tolerance)
                saw_err = saw_err or (err != 0)

        if saw_err and except_on_error:
            raise ValueError("some requested comparisons failed! See log")
        else:
            success_str = f'Comparison of these runners succeeded:\n'
            for name, runner, dur in zip(names, runners, durs):
                success_str += textwrap.indent(f'{name} : took {round(dur, 2)} s\n', '  ')
            logger.info(success_str)

        np.set_printoptions(threshold=1000) # the default, put it back

        # rekey for convenience
        return {n : vals for n, vals in zip(names, internals)}

class ComposedRunner(FemtoRunner):
    """create a new FemtoRunner object that strings one or more runners together

    The port maps allow for hooking up output names to input names

    Args:
        list_of_runners : (list of :obj:`FemtoRunner`) :
            list of femtorunners to stack in a sequence
        list_of_port_maps : (list of dicts, or None) :
            list of port maps, or None where a port map is not needed
            must be the same length as list_of_runners
            individual list elements may also be None if no mapping is needed for that layer
            [{output_i_name : input_i+1_name, ...}, ...]
    """
    def __init__(self, list_of_runners, list_of_port_maps=None):
        self.runners = list_of_runners
        self.port_maps = list_of_port_maps

    def reset(self, reset_vals=None):
        for runner in self.runners():
            runner.reset(reset_vals)

    def finish(self):
        for runner in self.runners:
            runner.finish()

    def step(self, input_vals):
        layer_inputs = input_vals
        all_internals = {}
        for i, runner in enumerate(self.runners):
            outputs, internals = runner.step(layer_inputs)

            if self.port_maps is not None and self.port_maps[i] is not None:
                layer_inputs = {}
                port_map = self.port_maps[i]
                for k, v in outputs.items():
                    layer_inputs[port_map[k]] = v
            else:
                layer_inputs = outputs

            for k, v in internals:
                if k in all_internals:
                    raise NotImplementedError("colliding state names in ComposedRunner, need to deal with this somehow")
                all_internals[k] = v

        return layer_inputs, all_internals
