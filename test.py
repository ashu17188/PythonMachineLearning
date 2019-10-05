#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:15:22 2019

@author: ashutosh shukla
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from subprocess import check_output
#print(check_output(["ls", "./datasets"]).decode("utf8"))

percentageOver25CompletedHighSchool = pd.read_csv('datasets/PercentOver25CompletedHighSchool.csv', encoding="windows-1252");

print(percentageOver25CompletedHighSchool.info())

sns.countplot(df=percentageOver25CompletedHighSchool);