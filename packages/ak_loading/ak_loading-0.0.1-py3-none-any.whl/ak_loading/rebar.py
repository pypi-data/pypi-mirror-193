#!/usr/bin/env python
# coding: utf-8

import pandas as pd

BAR_DF = pd.DataFrame({
    'bars': ['10M', '15M', '20M', '25M', '30M', '35M', '45M', '55M'],
    'dia': [11.3, 16, 19.5, 25.2, 29.9, 35.7, 43.7, 56.4],
    'area': [100, 200, 300, 500, 700, 1000, 1500, 2500],
    'hook_dia': [60, 90, 100, 150, 200, 250, 400, 550]
    })
BAR_DF = BAR_DF.set_index('bars')

WELD_XU={'E43XX':430, 'E49XX':490, 'E55XX':550, 'E62XX':620, 'E82XX':820}