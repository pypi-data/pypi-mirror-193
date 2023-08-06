#!/usr/bin/env python
# coding: utf-8

from ak_loading.rebar import *
import pandas as pd

def test_BAR_DF():
    type(BAR_DF) == pd.core.frame.DataFrame
    assert len(BAR_DF) == 8
    assert 'area' in BAR_DF.columns
    assert 'dia' in BAR_DF.columns
    assert 'hook_dia' in BAR_DF.columns
    assert BAR_DF.loc['10M', 'dia'] == 11.3
    assert BAR_DF.loc['25M', 'area'] == 500
    assert BAR_DF.loc['45M', 'hook_dia'] == 400

def test_BAR_DF_index():
    """Test that the 'bars' column is used as the index of the BAR_DF dataframe"""
    assert BAR_DF.index.name == 'bars'

def test_BAR_DF_columns():
    """Test that the BAR_DF dataframe contains the expected columns"""
    expected_columns = ['dia', 'area', 'hook_dia']
    assert set(BAR_DF.columns) == set(expected_columns)


def test_WELD_XU():
    type(WELD_XU) == dict
    WELD_XU.get('E43XX') == 430
    WELD_XU.get('E43XXX') == None
    WELD_XU.get('E82XX') == 820

    """Test that the WELD_XU dictionary has the expected keys and values"""
    expected_keys = ['E43XX', 'E49XX', 'E55XX', 'E62XX', 'E82XX']
    assert set(WELD_XU.keys()) == set(expected_keys)

    expected_values = [430, 490, 550, 620, 820]
    assert set(WELD_XU.values()) == set(expected_values)