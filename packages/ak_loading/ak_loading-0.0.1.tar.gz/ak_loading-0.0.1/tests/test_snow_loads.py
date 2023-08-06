from ak_loading.snow_loads import *
import pytest


def test_find_C_s_case_slippery_slope_15():
    expected = [r"Slope \leq 15 \degree", 1]
    assert find_C_s_case(15, True) == expected

def test_find_C_s_case_slippery_slope_60():
    expected = [r"15 \degree < Slope \leq 60 \degree", 0.6666666666666666]
    assert find_C_s_case(30, True) == expected

def test_find_C_s_case_slippery_slope_75():
    expected = [r"Slope > 60 \degree", 0]
    assert find_C_s_case(75, True) == expected

def test_find_C_s_case_not_slippery_slope_30():
    expected = [r"Slope \leq 30 \degree", 1]
    assert find_C_s_case(30, False) == expected

def test_find_C_s_case_not_slippery_slope_70():
    expected = [r"30 \degree < Slope \leq 70 \degree", 0.5]
    assert find_C_s_case(50, False) == expected

def test_find_C_s_case_not_slippery_slope_80():
    expected = [r"Slope > 70 \degree", 0]
    assert find_C_s_case(80, False) == expected