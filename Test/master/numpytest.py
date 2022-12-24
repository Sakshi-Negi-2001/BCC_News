# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:49:10 2019

@author: Naseem
"""
import pandas as pd
df=pd.read_csv("titanic.csv", header=0)
df.describe()
df["age"].hist()