"membuat program librabry numpy"
import numpy as np
"membuat program input untuk menambahkan nilai inputsnya"
inputs = [[1.6, 1.7, 1.4, 1.8,10.9, 1.2],
					 [0.21, 0.44, 0.13, 0.77, 0.66, 0.55],
					 [0.31, 0.51, 0.55, 0.99, 0.11, 0.45],
                     [0.41, 0.32, 0.66, 0.95, 0.24, 0.15],
                     [0.44, 0.56, 0.89, 0.31, 0.79, 0.26],
                     [0.43, 0.73, 0.33, 0.42, 0.67, 0.52],
					 [0.88, 0.63, 0.13, 0.43, 0.25, 0.86],
					 [0.66, 0.23, 0.21, 0.32, 0.35, 0.36],
                     [0.41, 0.21, 0.26, 0.29, 0.31, 0.87],
                     [0.89, 0.98, 0.21, 0.29, 0.26, 0.24]]
"membuat program weight untuk menambahkan weightsnya"                     
weights = [[0.77, 0.21, 0.65, 0.6, 0.9, 0.24],
					 [0.64, 0.88, 0.31, 0.64, 0.46, 0.18],
					 [0.12, 0.21, 0.29, 0.43, 0.64, 0.46],
                     [0.68, 0.51, 0.68, 0.31, 0.28, 0.54],
                     [0.76, 0.35, 0.38, 0.31, 0.56, 0.55]]
"membuat bias untuk dijumlahkan dengan inputs dan weightnya"                     
biases = [4.7, 2.0, 9.5, 4.7, 5.0]
"membuat program layer ouput untuk mengetahui hasil ouputs dari operasi yang telah dibuat"
layer_outputs = np.dot(inputs, np.array(weights).T) + biases 
print(layer_outputs)