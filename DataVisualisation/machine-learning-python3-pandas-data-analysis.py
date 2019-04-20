# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:32:53 2019

@author: Ashutosh Shukla
"""

import pandas as pd 
import sklearn
from sklearn.linear_model import SGDRegressor,SGDClassifier
from sklearn import svm , preprocessing

df = pd.read_csv("C:/Work/JavaProgram/PythonMachineLearning/datasets/diamonds.csv",index_col=0)

cut_class_dict={"Fair":1,"Good":2,"Very Good":3,"Premium":4,"Ideal":5}
clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL": 11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}

df['cut'] = df['cut'].map(cut_class_dict)
df['clarity'] = df['clarity'].map(clarity_dict)
df['color'] = df['color'].map(color_dict)
df.head()

df = sklearn.utils.shuffle(df) # always shuffle your data to avoid any biases that may emerge b/c of some order.

X = df.drop("price", axis=1).values
X = preprocessing.scale(X)
y = df["price"].values

print("X shape", X.shape)
print("y shape", df["price"].shape)

test_size=200
X_train = df[:-test_size]
y_train = df[:-test_size]

X_test =df[-test_size:]
y_test =df[-test_size:]

clf = SGDRegressor(max_iter=1000)
clf.fit(X_train, y_train)
print(clf.score(X_test,y_test))
