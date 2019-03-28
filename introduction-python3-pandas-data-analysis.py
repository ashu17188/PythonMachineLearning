# -*- coding: utf-8 -*-
"""
https://pythonprogramming.net/introduction-python3-pandas-data-analysis/
@author: Ashutosh Shukla
"""

import pandas as pd 

df = pd.read_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/avocado.csv");

graph_df = pd.DataFrame()
df=df.copy()[df['type']=='organic']
df['Date'] = pd.to_datetime(df['Date']);



#Fetch all unique values of a column  in dataframe
print(set(df['region']));
print(df.head())
#pass a parameter to the head, which is how many rows you want
print(df.head(1))
print(df.tail())
print("Last 2 rows" , df.tail(2))

df1 = df['AveragePrice'].head()
print(df1)

albany_df = df[df['region']=='Albany']
print(albany_df.head())

albany_df.set_index("Date",inplace=True)
print(albany_df.head())

albany_df.sort_index(inplace=True)
albany_df['price25ma'] =albany_df['AveragePrice'].rolling(25).mean()
albany_df['AveragePrice'].rolling(25).mean().plot();
print(albany_df.head())


for region in df['region'].unique()[:16]:
    print(region)
    region_df=df.copy()[df['region']==region]
    region_df.set_index('Date',inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"]=region_df['AveragePrice'].rolling(25).mean()
    
    if graph_df.empty:
        graph_df= region_df[[f"{region}_price25ma"]]
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])
graph_df.tail();

graph_df.plot(figsize=(8,5), legend=False)