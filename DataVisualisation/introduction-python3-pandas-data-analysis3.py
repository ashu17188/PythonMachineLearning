# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:01:47 2019

@author: Ashutosh Shukla
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/Minimum Wage Data.csv", encoding="latin");
df.to_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/minwage.csv", encoding="utf-8")


df = pd.read_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

act_min_wage.head()

min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

min_wage_corr.head()


plt.matshow(min_wage_corr)
plt.show()

