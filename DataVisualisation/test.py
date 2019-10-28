#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:07:37 2019

@author: administrator
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#print(os.listdir('../datasets'))
plt.figure(figsize=(12,7))
sns.set(style='whitegrid')
df = pd.read_csv('../datasets/StudentsPerformance.csv')

df.rename(columns=({'gender':'Gender','race/ethnicity':'Race/Ethnicity',
                   'parental level of education':'Parental_Level_Of_Education',
                   'lunch':'Lunch','test preparation course':'Test_Preparation_Course',
                   'math score':'Math_Score','reading score':'Reading_Score',
                   'writing score':'Writing_Score'}),inplace=True);

print(df['Test_Preparation_Course'].unique());

newDf =  df[df['Test_Preparation_Course']=='completed'].groupby(df['Lunch']).Writing_Score.sum();
print(newDf)
X=df.iloc[:,5]

Y= df.iloc[:,0]

h = df.iloc[:,2]

plt.legend(loc=0)
sns.barplot(x=newDf.index,y=newDf.values)
plt.xticks(rotation=45)
plt.title('Student performance report')
#Completed upto 33 
"""
gender                         object
race/ethnicity                 object
parental level of education    object
lunch                          object
test preparation course        object
math score                      int64
reading score                   int64
writing score                   int64
"""


