import numpy as np

# places the all the points on the unit hypershpere by making their magnitude to 1
def unitHyper(x):
    m,n = x.shape
    # for each point calculate the magnitude of it and divide it by magnitude
    for i in range(m):
        x[i] = x[i]/np.linalg.norm(x[i])
    return x



# creates the random matric with dimension N x C which is orthogonal
def rand_perm_mat(N,C):
    # creates a matrux with dimension N x C with all diaginal elements as 1
    I = np.eye(C,N)
    # creates a random permutation of C numbers
    p = np.random.permutation(np.arange(C))
    # selects the columns of I in the order of p and returns the matrix
    # which results a random rotation orthogonal matrix
    return I[p]