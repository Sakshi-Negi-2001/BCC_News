# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:37:20 2019

@author: Naseem
"""

from NaiveBayes import  Pool
import os
import json 

def getJson(data):
    res =[]
    for i in data:
        res.append({str(i[0]):i[1]})
    return json.dumps({"res":res})   

DClasses = ["medical",  "music", "business","entertainment","politics","sport","tech"]
TClasses = ["politics","music"]

base = "learn/"
p = Pool()
for i in DClasses:
    p.learn(base + i, i)



base = "test/"
for i in TClasses:
    dir = os.listdir(base + i)
    for file in dir:
        res = p.Probability(base + i + "/" + file)
        print(i + ": " + file + ": " + str(getJson(res))) 