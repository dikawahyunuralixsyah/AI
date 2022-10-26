#   membuat program untuk inisialisasi numpy
import numpy as np

# membuat program untuk variabel inputs
inputs	=  [[4.8, 7.7, 4.3, 2.1, 2.5, 4.7, 5.1 , 3.6, 7.6, 1.8],
            [6.4, 7.9, 6.2, 4.1, 3.1, 2.6, 7.1, 6.9, 5.5, 3.5],
            [4.2, 4.1, 1.4, 3.7, 5.2, 3.8, 9.1, 4.7, 7.4, 6.9],
            [6.5, 4.3, 2.2, 2.1, 1.6, 7, 7.8, 7.9, 4.7, 4.4],
            [2.3, 6.7, 7.8, 8.9, 9.1, 1.2, 2.3, 3.4, 4.5, 5.6],
            [5.3, 3.2, 2.1, 3.3, 7.5, 5.4, 4.7, 8.3, 9.7, 6.5]]

# membuat progarm weights untuk hidden layer 1 
weights =  [[0.12, 0.32, 0.48, 0.19, 0.53, 0.41, 0.61, 0.19, 0.17, 0.24],
            [0.70, 0.41, 0.22, 0.26, 0.34, 0.15, 0.24, 0.17, 0.98, 0.69],
            [0.80, 0.11, 0.31, 0.34, 0.39, 0.45, 0.16, 0.87, 0.48, 0.29],
            [0.9, 0.11, 0.22, 0.47, 0.14, 0.35, 0.42, 0.37, 0.47, 0.59],
            [0.20, 0.31, 0.54, 0.51, 0.49, 0.42, 0.58, 0.87, 0.99, 0.11]]

#membuat bias hidden layer 1
bias = [9, 2, 6, 7, 1]

#membuat program output hidden layer 1
output  = np.dot(inputs, np.array(weights).T) + bias

# membuat program untuk weights hidden layer 2
weights2 = [[0.14, 0.52, 0.43, 0.74, 0.65],
            [0.17, 0.83, 0.96, 0.23, 0.34],
            [0.32, 0.24, 0.11, 0.48, 0.29]]

# membuat bias hidden layer 2
bias2 = [4, 7, 8]

#membuat program output hidden layer 2
output2 = np.dot(output, np.array(weights2).T) + bias2	

# menyetak output
print(output2)
