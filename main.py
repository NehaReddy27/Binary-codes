

import numpy as np
from data_independent import algo1
from helper_functions import unitHyper
from helper_functions import rand_perm_mat
from data import getData
from results import write_to_file
from results import write_to_file_similarity
from graph import algo1Graph
import time

# gets data and lower dimensionality on which the data has to be represented
dense,lC = getData()
    
# places all on the ponits in the data on the unit hypershpere
dense = unitHyper(dense)

print(dense.shape)
print(dense[0])


#gets number of points in the data and dimension of them
n,d = dense.shape
# gets a random rotation matrix which is orthogonal
# along with rotation the dimension of the point is reduced to the specified
RT = rand_perm_mat(d,lC)





print(RT.shape,'RT shape')

# The main steps in the algorithm are performed for 6 times.
# the algorithm is said to converge in less than 5 times

for j in range(6):
    # In each step B is computed from R
    # B is initialized to empty
    B = []
    B1 = []
    # each column of B is calculated from each column of data and appended to matrix B
    # each column of B is obtained using algo1
    #step 1
    start = time.time()
    print('Iteration-',j+1)
    for i in range(len(dense)):
        if i ==0:
            B,B1 = algo1(np.matmul(RT,dense[i].T))
        else:
            A,A1 = algo1(np.matmul(RT,dense[i].T))
            B = np.append(B,A,1)
            B1 = np.append(B1,A1,1)
            
    #print(B.shape)
    
    #step 2
    X = dense.T
    # from svd of X * B.T matrix is calculated
    S = np.matmul(X,B.T)
    U, s, V = np.linalg.svd(S)
    # R is obtained by taking first lC singular vector of U
    # R is the product of Uc and V transpose
    R =  np.matmul(U[:,0:lC],V.T)
    RT = R.T
    done = time.time()    
    elapsed = done - start
    print('elapsed time: ',elapsed)
    RT = np.array(RT)
    #print(RT.shape)
    print(dense.shape,'dense shape')



B= B.T

# writes the original data points to a file
write_to_file("Original.csv",dense)



# writes the points obtained after mapping it to binary codes
write_to_file("Converted_512.csv",B)
    
    

# write the similarity between any two points after and before mapping
write_to_file_similarity("Similarity.csv",B,dense)

algo1Graph(np.matmul(RT,dense[0].T),1)
algo1Graph(dense[0].T,0)



