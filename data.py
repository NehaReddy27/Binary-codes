#returns the data

import h5py
import numpy as np


def getData():
    # reads the data from a file
	# mat file containing the feature vectors obtained from dense SIFT descriptors
    f = h5py.File('Ftraining_denseSIFT_split_01.mat','r') 
        
    arrays = {}
    for k, v in f.items():
        arrays[k] = np.array(v)

    # extracting the required data array
    dense = arrays['Ftraining'] 
	# printing the original data file size  
    print(dense.shape)
    # reshaping the data matrix
    dense = dense[0:1000,0:1000]
    print(dense.shape)
    
    #dense = dense[:,0:20000]
    lC = 200
	# lC is the num of dimensions after reducing the dimensionality
    return dense,lC
