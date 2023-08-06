from ak_loading.latexize import *
from handcalcs.decorator import handcalc
import pytest

def test_execute_handcalcs():
    @handcalc(precision=1)
    def f(x, y):
        z = x + y
        return locals()

    # Test that the function returns the correct output
    latex, values = execute_handcalcs(f, 2, 3)
    assert latex == "z &= x + y  = 2 + 3 &= 5"
    assert values == {"x": 2, "y": 3, "z": 5}

    # Test that the LaTeX string doesn't contain any extraneous characters
    assert r"\begin{aligned}" not in latex
    assert r"\end{aligned}" not in latex

    # Test that the function raises an error if it fails
    with pytest.raises(TypeError):
        execute_handcalcs(f, 2, "3")