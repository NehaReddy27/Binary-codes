# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:35:45 2017

@author: neha
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from data_independent import takeSecond
from data_independent import fun

def algo1Graph(x,t):
    l1 = []
    l2 = []
    #print(x.shape)
    X = []
    # for each feature in point index is added
    # this will be useful to know the original position of feature even after sorting
    for i in range(len(x)):
        t = (i,x[i])
        X.append(t)
    x = X
    # the point is sorted in the decreasing order of their feature values
    # takeSecond takes the feature value from the pair of index,feature value
    x.sort(reverse=True,key = takeSecond)
    m = 0
    k = 0
    # algorithm to find the nearest binary code for a point
    for i in range(len(x)):
        # the algorithm breaks when it sees a zero
        # because zeroes does not effect the simiarity in this formula
        if x[i][1] == 0:
            break
        # calculates the simialarity between the point and the point which have 1 at i largest positions of the point
        s = fun(x,i)/math.sqrt(i+1)
        l1.append(i+1)
        l2.append(s)
        if m < s:
            m = s
            k = i+1
    print('for thr below graph m=',k)
    plt.xlabel('sorted index k')
    if t==0:
        plt.ylabel('Y(x,k)')
    else:
        plt.ylabel('Y(RT*x,k)')
    plt.plot(l1,l2)
    plt.show() 
