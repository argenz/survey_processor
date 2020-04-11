#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:25:55 2019

@author: FCRA
"""

from gsheet_tools import Survey_Analytics 

#call class 
f = Survey_Analytics()

#call df for variable explorer 
#df = f.get_joined_dfs()

#show plots
make_plots = f.save_pn_plots()

