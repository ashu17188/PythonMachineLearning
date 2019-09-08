# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 13:37:29 2018
NumPy, which stands for Numerical Python, is a library consisting of 
multidimensional array objects and a collection of routines for processing 
those arrays. Using NumPy, mathematical and logical operations on arrays 
can be performed. 
"""

import numpy as np
import pandas as pd 
import seaborn as sns

#1.Creata a Dataframe from numpy arrays
dates = pd.date_range(20191010,periods=6)
print(df)

df= pd.DataFrame(np.random.randn(6,4),index=dates,
             columns=list('ABCD'))

print(df)
sns.countplot(x='A',data=df)