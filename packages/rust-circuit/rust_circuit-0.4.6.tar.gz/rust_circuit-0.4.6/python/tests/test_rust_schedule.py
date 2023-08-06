from typing import cast

import hypothesis
import torch
from torch.testing import assert_close

import rust_circuit as rc
from interp.circuit.testing.utils import mark_not_interesting_if
from rust_circuit import *

from .test_rust_rewrite import get_c_st

po = rc.PrintOptions(tensor_index_literal=True, bijection=False)


@hypothesis.settings(deadline=None)
@hypothesis.given(get_c_st(max_growth_steps=20))
@mark_not_interesting_if(SchedulingOOMError)
def test_schedule(circ):
    raw_test_schedule(circ)


def raw_test_schedule(circ):
    schedule = optimize_to_schedule(circ)
    hypothesis.note(circ.repr(po))
    # hypothesis.note(rc.optimize_circuit(circ).repr())

    hypothesis.assume(
        all(not ix.cast_index().has_tensor_axes() for ix in circ.get(rc.Index))
    )  # might go away due to Index.canonicalize, so can't replace them

    circ_out = circ.evaluate()
    assert_close(circ_out, schedule.evaluate().type(circ_out.dtype))

    circ_replaced = circ.update(rc.Array, lambda x: Array(cast(Array, x).value + 9.1))
    orig = circ_replaced.evaluate()
    circ_replaced_in_rust = schedule.replace_tensors(
        {x.hash: x.cast_array().value + 9.1 for x in rc.all_children(circ) if x.is_array()},
        allow_missing=True,  # FIXME remove allow_missing (need to debug)
    )
    assert_close(orig, circ_replaced_in_rust.evaluate().type(orig.dtype))
