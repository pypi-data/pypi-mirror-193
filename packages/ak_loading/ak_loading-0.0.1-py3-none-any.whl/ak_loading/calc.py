#!/usr/bin/env python
# coding: utf-8

import streamlit as st

class Values:
    def __init__(self, default_inputs:dict, app_title:str):
        self.default_inputs = default_inputs
        units, default_values = [], []
        
        for k, v in default_inputs:
            default_values[k], units[k] = v
            
        self.units = units
            
        self.app_title = app_title
        
        if not ('app_title' in st.session_state.keys() and st.session_state['app_title'] == app_title):
            "Clears the session state variables if the current loaded app is not in memory"
            clear_session_state()
            st.session_state['app_title'] = app_title
            
        #Session State consists of raw values
        update_sessionstate(default_values, override=False)
        #Session var contains units aware values
        self.var = {}
        
    def _update_var(self, calc_vars:dict={}):
        """Updates the session_state Variables. For key, value in session_state, if units exist for 
        key, make the session variable unitful. Additionally, if calc_vars are supplied add app_num 
        to key name and add to session variables
        """
        for var_key in st.session_state.keys():
            state_value = st.session_state[var_key]
            if type(state_value) in [int, float]:
                unit = self.units.get(var_key, 1)
                self.var[var_key] = state_value * unit
            else:
                self.var[var_key] = state_value
        
        for key, value in calc_vars.items():
            self.var[key] = value
                
    def getval(self, var:str):
        # self._update_var()
        # return self.var[var]
        return st.session_state[var] * self.units.get(var, 1)
    
    def __str__(self):
        return 'App Values - Default Inputs\n' + '\n'.join([f"{key}: {value}" for key, value in self.default_inputs.items()])
    
    def __repr__(self):
        units = self.units
        default_inputs=self.default_inputs
        app_title = self.app_title
        return f"app_value({units=}, {default_inputs=}, {app_title=})"
    
    def run_handcalc_function(self, function, *vars):
        self.latex, self.value = function(*vars)
        self._update_var(self.value)
        return self.latex, self.value
    
def update_sessionstate(values:dict, override:bool = False):
    "Updates the session_state variables; Typically used to set default values at init"
    current_session = st.session_state.keys()
    for key, value in values.items():
        if override or not (key in current_session):
            st.session_state[key] = value

def clear_session_state():
    "Clears the session state variables"
    for key in st.session_state.keys():
        del st.session_state[key]