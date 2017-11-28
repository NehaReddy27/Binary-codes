# finds the mapping of a point to binaru codes with data independent algorithm

import numpy as np
import math


def takeSecond(elem):
    return elem[1]

# funtion returns the sum of first k largest values in data point x    

def fun(x,k):
    s = 0;
    for i in range(k+1):
        s = s + x[i][1]
    return s

def algo1(x):
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
        if m < s:
            m = s
            k = i+1
    # forms the point with k ones at k largest positions of the point
    b = [0 for i in range(len(x))]
    for i in range(k+1):
        # x[i][0] represents the position of ith largest feature value in x
        # the corresponding position is made to 1
        # the magnitude of the point is made 1 
        b[x[i][0]] = 1/math.sqrt(k+1)
    
    b = np.matrix(b)
    # the point is returned as a column matrix
    return b.T