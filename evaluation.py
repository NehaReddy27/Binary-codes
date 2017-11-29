# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:51:26 2017

@author: neha
"""

# this file takes the modified vectors and for each vector it arranges the 
# ids of other vectors in decreasing order of similarity with the vector.

import pandas as pd
import numpy as np
import csv
import math

data = pd.read_csv("Converted_512.csv",header=0,delimiter=',')
ofile = open("Converted_top_512.csv","w")
writer = csv.writer(ofile,delimiter=",")

#data = data.iloc[0:10,:]

def takeSecond(elem):
    return elem[1]

#for each vector the similaity of it with oter vectors is calculated

for l1 in range(len(data)):
    row1 = data.iloc[l1]
    row1 = list(row1)
    l = []
    # for every other vector
    for l2 in range(len(data)):
        if l1!=l2:
            row2 = data.iloc[l2]
            row2 = list(row2)
            # similarity is computed using dit product.
            t = (l2,np.dot(row1,row2)/(math.sqrt(row1.count(1)*row2.count(1))))
            l.append(t)
    # the ids of vectors are sorted based on the similaity with the main vector.
    l.sort(reverse=True,key = takeSecond)
    #print(l)
    print(l1)
    # the list ois printed is printed to a file from whoch pr curves are ploted.
    l1 = [l[i][0] for i in range(len(l))]
    writer.writerow(l1)

ofile.close()