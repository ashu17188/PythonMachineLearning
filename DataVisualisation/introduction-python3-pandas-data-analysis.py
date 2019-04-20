# -*- coding: utf-8 -*-
"""
https://pythonprogramming.net/introduction-python3-pandas-data-analysis/
@author: Ashutosh Shukla
"""

import pandas as pd 

df = pd.read_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/avocado.csv");

df['Date']= pd.to_datetime(df['Date'])
albany_df = df[df['region']=="Albany"];



albany_df.set_index("Date",inplace=True)
albany_df.sort_index(inplace=True)
albany_df['AveragePrice'].rolling(25).mean().plot()

#ploting distribution with respect to all region


