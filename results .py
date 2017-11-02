# prints the data to file

import numpy as np
import csv

# write each row of the matrix as a row to csv file
def write_to_file(T,matrix_value):
	ofile = open(T,"w")
	writer = csv.writer(ofile,delimiter=",")
	K = np.asarray(matrix_value)
	for i in range(len(K)):
	    #print(dense[i])
	    writer.writerow(K[i])

	ofile.close()
    

# find the similarity between any two points and writes to a file
    
def write_to_file_similarity(T,B,D):
    ofile = open(T,"w")
    writer = csv.writer(ofile,delimiter=",")
    l = ['Binary codes similarity']
    # for each two points calculate the similarity
    # product of the two gives similarity as there unti vectors
    for i in range(len(B)):
        for j in range(i+1,len(B)):
            k = np.array(B[i]*B[j].T)
            #print(k[0][0])
            l.append(k[0][0])
    # 1st row is the similarity after mapping
    writer.writerow(l)
    
    D = np.matrix(D)
    l = ['Original points similarity']
    # for each two points calculate the similarity
    # product of the two gives similarity as there unti vectors
    for i in range(len(D)):
        for j in range(i+1,len(D)):
            k = np.array(D[i]*D[j].T)
            l.append(k[0][0])
    
    # 2nd row is the similarity before mapping
    writer.writerow(l)
    
    ofile.close()