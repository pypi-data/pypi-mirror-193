#!/usr/bin/env python
# coding: utf-8

from ak_loading.latexize import execute_handcalcs

from dataclasses import dataclass, asdict
from pathlib import Path
import pandas as pd
from math import atan, degrees, exp


from handcalcs.decorator import handcalc
import forallpeople
forallpeople.environment('structural', top_level=True)

_SNOW_DATAPATH = Path(__file__).parent / "snow_data.pkl"

@dataclass
class SnowLoadInput:
    S_s: forallpeople.Physical
    S_r: forallpeople.Physical
    I_s: float
    C_b: float
    C_w: float
    C_a: float
    pitch: float
    slippery: bool
    
    def dict(self) -> dict:
        return asdict(self)

class MasterCalc:
    def __init__(self, inputs):
        self.values = inputs

    def __repr__(self) -> str:
        return "MasterCalc()"

    def _get_latex(self, function, *args, **kwargs) -> str:
        """Generates the latex str of the given function and updates the `self.values`
        attributes to the result of the funtion execution.
        """
        latex, values = execute_handcalcs(function, *args, **kwargs)
        self._set_values(values)
        return latex

    def _set_values(self, values: dict) -> None:
        "Update `self.values` attribute from dict"
        for key, value in values.items():
            setattr(self.values, key, value)

class SnowLoad(MasterCalc):
    def __init__(self, inputs: SnowLoadInput):
        MasterCalc.__init__(self, inputs)
        self.data = pd.read_pickle(_SNOW_DATAPATH)
    
    def __str__(self) -> str:
        return f"SnowLoad Class for design of slab"

    def __repr__(self) -> str:
        return self.values.__repr__()

    def section_1_specified_snow_load(self) -> str:
        values = self.values
        latex_lines = []        #Collect all lines of latex to be joined together at end

        latex_lines.append("S_{s} &= " + f"{self.values.S_s:.2f}")
        latex_lines.append("S_{r} &= " + f"{self.values.S_r:.2f}")
        latex_lines.append("I_{s} &= " + f"{self.values.I_s:.2f}")

        #Calculate C_s
        slope = degrees(atan(values.pitch/12))      #In degrees
        latex_lines.append(f"Slippery\\ Roof &= {values.slippery}")
        latex_lines.append(f"Roof\\ Slope &= {slope:.2f} \\degree")
        latex, self.values.C_s = find_C_s_case(slope, values.slippery)
        latex_lines.append(latex)
        latex_lines.append(f'C_s &= {self.values.C_s:.2f}')

        #Calculate Specified Snow Load
        latex = self._get_latex(
            calculate_S,
            I_s=self.values.I_s, 
            S_s=self.values.S_s,
            S_r=self.values.S_r,
            C_b=self.values.C_b,
            C_w=self.values.C_w,
            C_s=self.values.C_s,
            C_a=self.values.C_a
            )
        latex_lines.append(
            self._get_latex(
                calculate_S,
                I_s=self.values.I_s, 
                S_s=self.values.S_s,
                S_r=self.values.S_r,
                C_b=self.values.C_b,
                C_w=self.values.C_w,
                C_s=self.values.C_s,
                C_a=self.values.C_a
            )
        )

        return latex_from_lines(latex_lines)

@dataclass
class Calc_CbInput:
    l: forallpeople.Physical
    w: forallpeople.Physical
    C_w: float

class Calc_Cb(MasterCalc):
    def __init__(self, inputs):
        MasterCalc.__init__(self, inputs)
    
    def section_1_basic_snow_load_factor(self) -> str:
        values = self.values
        latex_lines = []        #Collect all lines of latex to be joined together at end

        #Calculate l_c
        latex_lines.append(
            self._get_latex(
                calculate_l_c, 
                max(values.l, values.w),
                min(values.l, values.w)
            )
        )

        if values.l_c < 70 / (values.C_w ** 2):
            latex_lines.append(r"Since,\ \ l_c < \frac{70}{C_w^{2}}")
            latex_lines.append("C_b = 0.8")
            values.C_b = 0.8
        else:
            latex_lines.append(r"Since,\ \ l_c \geq \frac{70}{C_w^{2}}")
            #Calculate C_b
            latex_lines.append(
                values._get_latex(
                    calculate_C_b, 
                    values.C_w,
                    values.l_c
                )
            )

        self.values = values
        return latex_from_lines(latex_lines)

def latex_from_lines(latex_lines: list) -> str:
    "Combines a list of latex lines into a single latex string"
    combined_latex = " \n\\\\[10pt]\n".join(latex_lines)
    return r'\begin{aligned}' + '\n' + combined_latex + '\n' + r'\end{aligned}'

def get_locations() -> dict:
    df = pd.read_pickle(_SNOW_DATAPATH)
    return df



def find_C_s_case(slope: float, slippery:bool) -> list[str, float]:
    "Returns the controlling case and the C_s value"
    if slippery:
        if slope <= 15:
            return [r"Slope \leq 15 \degree", 1]
        elif slope <= 60:
            return [r"15 \degree < Slope \leq 60 \degree", (60 - slope)/45]
        else:
            return [r"Slope > 60 \degree", 0]
    else:
        if slope <= 30:
            return[r"Slope \leq 30 \degree",1]
        elif slope <= 70:
            return [r"30 \degree < Slope \leq 70 \degree", (70 - slope)/40]
        else:
            return [r"Slope > 70 \degree", 0]

# <!---------------- HANDCALC FUNCTIONS ---------------->
@handcalc(precision=2, override="long")
def calculate_C_b(C_w, l_c):
    C_b = 1/C_w * (1 - ((1- 0.8 * C_w) * exp(-(C_w**2*l_c/m - 70)/100)))
    return locals()

@handcalc(precision=2, override="long")
def calculate_l_c(l,w):
    l_c = 2 * w - (w**2 / l)
    return locals()
    
@handcalc(precision=2, override="long")
def calculate_S(I_s, S_s, S_r, C_b, C_w, C_s, C_a):
    S_ULS = I_s * (S_s * (C_b * C_w * C_s * C_a) + S_r)
    S_SLS = 0.9 * (S_s * (C_b * C_w * C_s * C_a) + S_r)
    return locals()