# Binary-codes
Angular Quantization-based Binary Codes for Fast Similarity Search

An implementation of Angular Quantization-based Binary Codes for Fast Similarity ,Yunchao Gong,Sanjiv Kuma,Vishal Verma,Svetlana Lazebnik  Google Research, New York, NY 10011, USA

Angular Quantization-based Binary coding (AQBC) technique is used in order to map the original high-dimensional data to similarity-preserving binary codes (learn binary codes for non-negative data with cosine similarity).

Two main bottlenecks in building an efficient retrieval system for high-dimensional data are the storage of huge database and the slow speed of retrieval which are handled by AQBC technique.

## DataSet
SUN Database - scene categorization data is chosen.There are about 19850 number of images.Each image is of 6300 dimensions. Each image is represented by feature vector computed on top of dense SIFT descriptors. In this method we are reducing the number of dimensions to 5000.
ReadMe will be updated as we try on more datasets.

Link : http://vision.princeton.edu/projects/2010/SUN/SUN397feature/

## Compile
Download the zipped file and use python main.py after unzipping in order to run the code.
Python version 3.4 is used. 

## Time Complexity
AQBC technique takes O(nc logc) + O(dc^2) time in order to obtain the binary codes of dimension c which is less d where d is the dimension of original dataset.
