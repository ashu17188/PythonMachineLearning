#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:07:37 2019

@author: administrator
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from subprocess import check_output
import numpy as np

#print(check_output(["ls", "./datasets"]).decode("utf8"))

kill = pd.read_csv('../datasets/PoliceKillingsUS.csv', encoding="windows-1252");
#print(kill.info());
#sns.countplot(x='age',data=kill);
sns.barplot(x='age',y='city',data=kill)