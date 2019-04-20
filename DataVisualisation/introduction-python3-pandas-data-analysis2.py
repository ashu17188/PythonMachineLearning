# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:54:44 2019

@author: Ashutosh Shukla
"""


import pandas as pd 

df = pd.read_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/avocado.csv");

df = df.copy()[df['type']=='organic']

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by="Date", ascending=True, inplace=True)
#df.head()

graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets! (so df rather than series)
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

graph_df.tail()

graph_df.plot(figsize=(8,5), legend=False)