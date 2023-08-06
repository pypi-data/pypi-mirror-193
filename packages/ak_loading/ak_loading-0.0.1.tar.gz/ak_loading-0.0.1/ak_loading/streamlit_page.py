#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import json
import ak_loading.html as ht
from datetime import datetime
from dataclasses import dataclass
from typing import Union

@dataclass
class Container:
    inputs: Union[None, st.delta_generator.DeltaGenerator]
    results: Union[None, st.delta_generator.DeltaGenerator]
    results_check: Union[None, st.delta_generator.DeltaGenerator]
    results_summary: Union[None, st.delta_generator.DeltaGenerator]
    calc: Union[None, st.delta_generator.DeltaGenerator]

class PageLayout:
    def __init__(self, 
                 title: str, 
                 hide_streamlit_footer:bool = False, 
                 custom_footer: str = None, 
                 remove_padding_from_sides: bool = False,
                 hide_sidebar:bool=False,
                 default_inputs: dict = {}):
        """Sets the Page title and default session state values

        Args:
            title (str): Page Title
            default_session_key_values (dict, optional): Dict of startup sessionstate keys and values, Defaults to {}
        """
        self.hide_streamlit_footer = hide_streamlit_footer
        self.custom_footer = custom_footer
        self.remove_padding_from_sides = remove_padding_from_sides
        self.title = title
        self.hide_sidebar=hide_sidebar
        self.default_inputs = default_inputs
        

        
        if not ('app_title' in st.session_state.keys() and st.session_state['app_title'] == title):
            "Clears the session state variables if the current loaded app is not in memory"
            clear_session_state()
            st.session_state['app_title'] = title
            
            for k,v in default_inputs.items():
                st.session_state[k] = v
    
        self.apply_layout()


    def __repr__(self):
        hide_streamlit_footer = self.hide_streamlit_footer
        custom_footer = self.custom_footer
        remove_padding_from_sides = self.remove_padding_from_sides
        title = self.title
        hide_sidebar = self.hide_sidebar
        return f"PageLayout({title=},{hide_streamlit_footer=},{custom_footer=},{remove_padding_from_sides=},{hide_sidebar=})"
    
    def apply_layout(self):
        st.header(self.title)
        if self.hide_streamlit_footer:
            st.markdown(ht.HIDE_STREAMLIT_FOOTER,unsafe_allow_html = True) 
        if self.custom_footer:
            html = self.custom_footer
            st.markdown(f"{ht.ADD_FOOTER['start']}{html}{ht.ADD_FOOTER['end']}" ,unsafe_allow_html=True)
        if self.remove_padding_from_sides:
            st.markdown(ht.REMOVE_PADDING_FROM_SIDES, unsafe_allow_html=True)
        if self.hide_sidebar:
            st.markdown(ht.HIDE_SIDEBAR, unsafe_allow_html=True)
            
        
    def setup_outline(
        self, 
        inputs:bool =True, 
        results: bool=True, 
        calculations:bool=True, 
        checks_and_summary_within_results:bool =True) -> Container:
        """Sets up the initial outline of the document with `Inputs`, `Results` and `Calculations` 
        and relevant containers.

        Returns:
            list[st.container]: A list of `Inputs`, `Results`, `Results-Summary`, `Results-Checks` and `Calculations` container
        """

        if inputs:
            st.subheader('Inputs')
            inputs_container = st.container()
            st.markdown('----')
        else:
            inputs_container = None
        
        if results:
            st.subheader('Results')
            results_container = st.container()
            if checks_and_summary_within_results:
                with results_container:
                    summary_container, checks_container = st.columns(2)
            else:
                summary_container, checks_container = None, None
            self.checks_html = ""
            self.summary_html = ""
            st.markdown('----')
        else:
            results_container, summary_container, checks_container = None, None, None
        
        if calculations: 
            st.subheader('Calculations')
            calc_container = st.container()
            st.markdown('----')
        else:
            calc_container = None

        self.container = Container(
            inputs = inputs_container,
            results=results_container,
            results_check=checks_container,
            results_summary=summary_container,
            calc = calc_container
        )
        return self.container

    @staticmethod
    def calc_section_w_status(head_container, title):
        """Creates a sub-container under the passed head container, Adds title and creates space for defining status of the following checks

        Args:
            head_container (streamlit container): container under which the sub-container is to be created
            title (str): Title in markdown format

        Returns:
            subcontainer, status_col: The created sub container and the column taking in status
        """
        sub_container = head_container.container()
        title_col, status_col = sub_container.columns(2)
        title_col.markdown(title)
        return sub_container, status_col

    @staticmethod
    def update_container_status(status_col, 
                      status="Pass", 
                      failure_note="Check Failed", 
                      success_note="Check Passed",
                      warn_note="Some Issue encontered"):
        """Updated the status column (created under `self.add_sub_container_w_status) with the passed value

        Args:
            status_col (streamlit column): streamlit column/container
            status (str, optional): Can be one of ["Pass","Fail","Warn"]. Defaults to "Pass".
            failure_note (str, optional): Note to show on "Fail". Defaults to "Check Failed".
            success_note (str, optional): Note to show on "Pass". Defaults to "Check Passed".
            warn_note (str, optional): Note to show on "Warn". Defaults to "Some Issue encontered".
        """
        assert status.strip().lower() in ['pass', 'fail', 'warn'], f"`{status}` is not a recognized option. Check Docstring"
        
        if status.lower().strip() == 'pass':
            status_col.success(success_note)
        elif status.lower().strip() == 'fail':
            status_col.error(failure_note)
        elif status.lower().strip() == 'warn':
            status_col.warning(warn_note)

    def checks_container_add(self, title: str,utilization):
        """Takes the Check title and the utilization (can be float, int or "Fail") and adds it to the `.checks_html` attribute, initializes html on first run

        Args:
            title (str): Check title
            utilization (float, int, "Fail"): Utilization to display on the table
        """
        
        if self.checks_html == "":
            self.checks_html = ht.CHECKS_TABLE_HTML_HEADER
        if type(utilization) != str:
            if utilization > 1:
                tag_class = "fail"
            elif utilization < 1:
                tag_class = "pass"
            else:
                tag_class = "warn"
            utilization = round(utilization*100,1)
            self.checks_html += (f'<tr><td>{title}</td><td style="text-align: center;" class="{tag_class}">{utilization}%</td></tr>')

        else:
            tag_class = utilization.lower().strip()
            self.checks_html += (f'<tr><td>{title}</td><td style="text-align: center;" class="{tag_class}">{utilization}</td></tr>')
        
        return None

    def resultsummary_add(self, title: str,value: str):
        """Takes the Summary Title and value and adds it to the `.summary_html` attribute, initializes html on first run
        """
        
        if self.summary_html == "":
            self.summary_html = """
            <table align="center" border="1" cellpadding="1" cellspacing="1"><tbody>
            """

        self.summary_html += (f'<tr><td scope="col">{title}</td><td scope="col">{value}</td></tr>')
        return None
    
    def final_cleanup(self):
        #Display the checks table
        if self.container.results_check and self.checks_html != "":
            self.checks_html += "</tbody></table>"
            self.container.results_check.write(self.checks_html, unsafe_allow_html=True)
        #Display summary_table
        if self.container.results_summary and self.summary_html != "":
            self.summary_html += "</tbody></table>"
            self.container.results_summary.write(self.summary_html, unsafe_allow_html=True)

            

    @staticmethod
    def formula_add(container, latex, prefix=None, suffix = None):
        """ Writes calculation latex along with any prefix(calc explanation) or suffix (calc reference) to the passed container
            If no prefix or suffix passed, latex is centered on page; 
            If both prefix else suffix passed, columns are split in the 1:3:1 ratio
            If only one of prefix or suffix passed, columns split into 1:4 (or 4:1) ratio

        Args:
            container (streamlit container): streamlit container to write the items to
            latex (str): Latex string/formula to write
            prefix (str, optional): string to write to prefix. Defaults to None.
            suffix (str, optional): string to write to suffix. Defaults to None.
        """
        if prefix != None and suffix != None:
            prefix_col, formula_col, suffix_col = container.columns([1,3,1])
        elif prefix != None or suffix != None:
            if prefix:
                prefix_col, formula_col = container.columns([1,4])
            else:
                formula_col, suffix_col = container.columns([4,1])
        else:
            formula_col = container
        
        if prefix:
            prefix_col.write(prefix)
        if suffix:
            suffix_col.write(suffix)
        
        formula_col.latex(latex)
    

    @staticmethod
    def add_inputs_export_import_to_sidebar(title: str) -> None:
        st.sidebar.markdown("------")
        st.sidebar.download_button(
            label="Export Variables",
            help=f"Export the variables for {title}",
            file_name=f"{title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            data=json.dumps(st.session_state, indent=4))
        st.sidebar.markdown("------")
        
        uploaded_file = st.sidebar.file_uploader(label="Upload inputs",
                                                type = "json",
                                                help="Import previously used inputs",
                                                accept_multiple_files=False)
        if uploaded_file is not None:
            #bytes_data = uploaded_file.getvalue()
            input = json.load(uploaded_file)
            
            def _update_inputs():
                for key, value in input.items():
                    st.session_state[key] = value
                return

            st.sidebar.button(label="Update",
                            on_click=_update_inputs,
                            key="update_button")

def clear_session_state():
    "Clears the session state variables"
    for key in st.session_state.keys():
        del st.session_state[key]