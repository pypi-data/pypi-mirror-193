#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from ak_loading.streamlit_page import PageLayout
from ak_loading.snow_loads import (
    SnowLoad, SnowLoadInput, get_locations, Calc_Cb, Calc_CbInput)
import forallpeople as si
si.environment('structural', top_level=False)

# <!------ Page Configs ------>
PAGE_TITLE = 'Snow Load Calculations'

st.set_page_config(
        page_title=PAGE_TITLE,
        layout="wide",
        page_icon='👨‍🔬',
        initial_sidebar_state="expanded")

default_inputs = {
    'location_data': 'Province/City',
    'province': 'British Columbia',
    'city': '100 Mile House',
    'importance': 'Normal',
    'C_w': 1.0,
    'C_a': 1.0,
    'C_b_calc': '0.8',
    'pitch': 0,
    'slippery': False
    }

for key, value in default_inputs.items():
    if not key in st.session_state.keys():
        st.session_state[key] = value

page = PageLayout( title=PAGE_TITLE,
                   hide_streamlit_footer=False,
                   custom_footer='Developed by <a href="https://linkedin.com/in/rpakishore" target="_blank">Arun Kishore</a>',
                   remove_padding_from_sides=True,
                   hide_sidebar=False,
                   default_inputs=default_inputs)

containers = page.setup_outline(
    inputs=True, 
    results=True, 
    calculations=True, 
    checks_and_summary_within_results=True)

snow_data = get_locations()

with containers.inputs:
    left, right = st.columns(2)
    with left:
        st.radio("Location Data", ['Coordinates', 'Province/City', 'Ground Snow/Rain Load'], key="location_data")

        if st.session_state.location_data == "Province/City":
            provinces = snow_data.loc[:, 'province'].unique()
            st.selectbox("Province", options=provinces, key="province")
            city = snow_data[snow_data['province'] == st.session_state.province].loc[:, 'location']
            st.selectbox("City", list(city), key="city")
            data = snow_data.loc[(snow_data['province'] == st.session_state.province) & (snow_data['location'] == st.session_state.city)]
            st.session_state.S_s = float(data.loc[:,'Ss'].iloc[0])
            st.session_state.S_r = float(data.loc[:,'Sr'].iloc[0])
        
        elif st.session_state.location_data == 'Ground Snow/Rain Load':
            st.number_input("Ground Snow Load, Ss | kPa", min_value=0.00, max_value=3.00, key='S_s')
            st.number_input("Rain Load, Ss | kPa", min_value=0.00, max_value=3.00, key='S_r')

        elif st.session_state.location_data == 'Coordinates':
            st.number_input("Latitude", min_value=-90.0000000, max_value=90.0000000, key='lat')
            st.number_input("Rain Load, Ss | kPa", min_value=-180.0000000, max_value=180.0000000, key='long')

        st.number_input("Wind exposure factor (Cw)", min_value=0.00, max_value=1.00, key='C_w')
        st.number_input("Snow accumulation factor (Ca)", min_value=0.00, max_value=1.00, key='C_a')

    with right:
        importance_factors = ['Low', 'Normal', 'High', 'Post Disaster']
        st.radio("Importance Factor", importance_factors, key="importance")
        st.session_state.I_s = [0.8, 1.0, 1.15, 1.25][importance_factors.index(st.session_state.importance)]

        st.radio("Basic Snow Load Factor (Cb)", ['0.8', 'Calculate from roof geometry', 'User Value'], key="C_b_calc")
        if st.session_state.C_b_calc == "0.8":
            st.session_state.C_b = 0.8
        elif st.session_state.C_b_calc == 'User Value':
            st.number_input("Basic Snow Load Factor (Cb)", min_value=0.00, max_value=1.00, key='C_b')
        elif st.session_state.C_b_calc == 'Calculate from roof geometry':
            st.number_input("Longer dimension (l) | m", min_value=0.10, key='l')
            st.number_input("Smaller dimension (w) | m", min_value=0.10, key='w')
            C_b_inputs = Calc_CbInput( 
                l = st.session_state.l * si.m, 
                w = st.session_state.w * si.m, 
                C_w = st.session_state.C_w)
            C_b_app = Calc_Cb(C_b_inputs)

        st.number_input("Roof Pitch (Pitch) | /12", min_value=0.00, max_value=12.00, key='pitch')
        st.checkbox("Slippery?", key="slippery")

inputs = SnowLoadInput(
    S_s=st.session_state.S_s*si.kPa,
    S_r=st.session_state.S_r*si.kPa,
    I_s=st.session_state.I_s,
    C_b=st.session_state.C_b,
    C_w=st.session_state.C_w,
    C_a=st.session_state.C_a,
    pitch=st.session_state.pitch,
    slippery=st.session_state.slippery)
app = SnowLoad(inputs=inputs)

## <!-------- Section 1 - Specified Snow Load -------->
section1 = containers.calc.container()
section1.markdown('#### Specified Snow Load')

if st.session_state.C_b_calc == 'Calculate from roof geometry':
    section1.markdown("##### Characteristic length of the roof")
    page.formula_add(
        container=section1,
        latex = C_b_app.section_1_basic_snow_load_factor()
        )


page.formula_add(
    container=section1,
    latex = app.section_1_specified_snow_load()
    )

page.resultsummary_add(title="Specific Snow Load (ULS):", value=app.values.S_ULS)
page.resultsummary_add(title="Specific Snow Load (SLS):", value=app.values.S_SLS)

# <!-------- Finish up -------->
page.final_cleanup()