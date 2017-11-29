# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:17:20 2017

@author: neha
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:47:29 2017

@author: neha
"""

# this file id used to plot presision recall curves for different bits 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv("Original_top.csv",header=0,delimiter=',')
data2 = pd.read_csv("Converted_top_1000.csv",header=0,delimiter=',')

c = 10

# precison and recall are calculated at each point until 10 vectors.

pr = [[] for i in range(c)]
re = [[] for i in range(c)]

for l1 in range(len(data1)):
    row1 = data1.iloc[l1,0:c]
    row1 = list(row1)
    row2 = data2.iloc[l1,0:c]
    row2 = list(row2)
    # 10 points or precison recall are obtained
    for i in range(c):
        t = []
        for j in range(i+1):
            t.append(row2[j])
        count = 0
        for k in range(len(t)):
            if t[k] in row1:
                count = count + 1
        
        pr[i].append((count*1.00)/(i+1))
        re[i].append((count*1.00)/len(row2))


y = []
z = []
# average of the pr is plted
for i in range(c):
    y.append(sum(pr[i])/float(len(pr[i])))
    z.append(sum(re[i])/float(len(re[i])))

#print(len(y))
    

#print(len(x))
fig = plt.figure()
#ax = plt.axes()

plt.plot(z,y,'-b')
plt.title("Precision-Recall curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
#fig.savefig("precision_recall.png")
#plt.show()
data2 = pd.read_csv("Converted_top_512.csv",header=0,delimiter=',')


pr = [[] for i in range(c)]
re = [[] for i in range(c)]

for l1 in range(len(data1)):
    row1 = data1.iloc[l1,0:c]
    row1 = list(row1)
    row2 = data2.iloc[l1,0:c]
    row2 = list(row2)
    for i in range(c):
        t = []
        for j in range(i+1):
            t.append(row2[j])
        count = 0
        for k in range(len(t)):
            if t[k] in row1:
                count = count + 1
        
        pr[i].append((count*1.00)/(i+1))
        re[i].append((count*1.00)/len(row2))


y = []
z = []
for i in range(c):
    y.append(sum(pr[i])/float(len(pr[i])))
    z.append(sum(re[i])/float(len(re[i])))
    

plt.plot(z,y,'-c')

data2 = pd.read_csv("Converted_top_256.csv",header=0,delimiter=',')


pr = [[] for i in range(c)]
re = [[] for i in range(c)]

for l1 in range(len(data1)):
    row1 = data1.iloc[l1,0:c]
    row1 = list(row1)
    row2 = data2.iloc[l1,0:c]
    row2 = list(row2)
    for i in range(c):
        t = []
        for j in range(i+1):
            t.append(row2[j])
        count = 0
        for k in range(len(t)):
            if t[k] in row1:
                count = count + 1
        
        pr[i].append((count*1.00)/(i+1))
        re[i].append((count*1.00)/len(row2))


y = []
z = []
for i in range(c):
    y.append(sum(pr[i])/float(len(pr[i])))
    z.append(sum(re[i])/float(len(re[i])))

plt.plot(z,y,'-g')


data2 = pd.read_csv("Converted_top_64.csv",header=0,delimiter=',')


pr = [[] for i in range(c)]
re = [[] for i in range(c)]

for l1 in range(len(data1)):
    row1 = data1.iloc[l1,0:c]
    row1 = list(row1)
    row2 = data2.iloc[l1,0:c]
    row2 = list(row2)
    for i in range(c):
        t = []
        for j in range(i+1):
            t.append(row2[j])
        count = 0
        for k in range(len(t)):
            if t[k] in row1:
                count = count + 1
        
        pr[i].append((count*1.00)/(i+1))
        re[i].append((count*1.00)/len(row2))


y = []
z = []
for i in range(c):
    y.append(sum(pr[i])/float(len(pr[i])))
    z.append(sum(re[i])/float(len(re[i])))
    

plt.plot(z,y,'-r')


plt.legend(['1000', '512', '256', '64'], loc='upper right')


plt.show()
