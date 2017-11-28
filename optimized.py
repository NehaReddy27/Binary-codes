
# In[1]:
    
#parallelized code    

from sklearn.datasets import fetch_20newsgroups
import numpy as np
import math
import time
from sklearn.utils.extmath import randomized_svd
from sklearn.decomposition import TruncatedSVD
from multiprocessing.pool import ThreadPool



# In[3]:

#newsgroups_test = fetch_20newsgroups(subset='test')
#print(newsgroups_test.filenames.shape)


# In[18]:

import h5py 
import numpy as np
f = h5py.File('Ftraining_denseSIFT_split_01.mat','r') 


arrays = {}
for k, v in f.items():
    arrays[k] = np.array(v)

dense = arrays['Ftraining']
print(dense.shape)

dense = dense[0:1000,0:1000]
print(dense.shape)

#dense = dense[:,0:20000]
lC = 512

# In[11]:
    
def unitHyper(x):
    m,n = x.shape
    for i in range(m):
        x[i] = x[i]/np.linalg.norm(x[i])
    return x

dense = unitHyper(dense)

print(dense.shape)
print(dense[0])

def rand_perm_mat(N,C):
    I = np.eye(C,N)
    p = np.random.permutation(np.arange(C))
    return I[p]

n,d = dense.shape
RT = rand_perm_mat(d,lC)
# In[12]:


def fun(x,k):
    s = 0;
    for i in range(k+1):
        s = s + x[i][1]
    return s

def takeSecond(elem):
    return elem[1]

def algo1(x):
    #print(x.shape)
    y = np.argsort(x)[::-1]
    x1 = np.sort(x)[::-1]
    cum = np.cumsum(x1)
    
    m = 0
    k = 0
    for i in range(len(x)):
        if x[y[i]] == 0:
            break
        s = cum[i]/math.sqrt(i+1)
        if m < s:
            m = s
            k = i+1
    b = np.zeros(len(x))
    b1 = np.zeros(len(x))
    #b = [0 for i in range(len(x))]
    #b1 = [0 for i in range(len(x))]
    for i in range(k):
        b[y[i]] = 1/math.sqrt(k+1)
        b1[y[i]] = 1
    #b = np.matrix(b)
    #b1 = np.matrix(b1)
    return b,b1



print(RT.shape,'RT shape')

for j in range(6):
    B = []
    B1 = []
    print('Iteration-',j+1)
    start = time.time()
    
    # 10 thread pool is created
    pool = ThreadPool(10) 
    results = []
    
    # each thread computes a column independently
    for i in range(len(dense)):
        x = np.matmul(RT,dense[i].T)
        results.append(pool.apply_async(algo1,args=(x,)))
    pool.close()
    pool.join()
    #print(results[1].get())
    B = []
    B1 = []
    i = 0;
    
    # append the results of all threads based on the order
    for r in results:
        b1,b2 = r.get()
        B.append(list(b1))
        B1.append(list(b2))
    B = np.array(B)
    B1 = np.array(B1)
    B = B.T
    B1 = B1.T
    #print(B.shape)
    #print(B)
    #results = [r.get() for r in results]
    #B = results
    
    #done = time.time()     
    #elapsed = done - start
    #print('elapsed time: ',elapsed)
    
    print(B.shape)
    X = dense.T
    
    start = time.time()
    S = np.matmul(X,B.T)
    U, s, V = np.linalg.svd(S)
    #U, s, V = sparsesvd(S,512)
    
    
    R =  np.matmul(U[:,0:lC],V.T)
    RT = R.T
    done = time.time()    
    elapsed = done - start
    print('elapsed time: ',elapsed)
    
    RT = np.array(RT)
    print(RT.shape)
    #print(dense.shape,'dense shape')



