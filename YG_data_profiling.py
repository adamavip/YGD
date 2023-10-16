# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:14:02 2023

@author: Adama
"""
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport

survey = pd.read_csv(r"C:\Users\Adama\OneDrive - CIMMYT\Documents\Code\R\EiA\input\#-master-hh-file.csv")
vars_survey = ["count_infants", "count_children_2_4", "count_children_5_14",\
               "count_adults", "methods_landprep", "machinery_cropmgt_use",\
               "machinery_cropmgt_types", "machinery_cropmgt_access", \
               "machinery_cropmgt_constraint","access_fertilizers", \
               "constraint_fertilizers", "access_organic_inputs",\
               "constraint_organic_inputs", "quality_rapport", "quality_reliability"]
survey = survey.loc[:, vars_survey]

ProfileReport(survey)
