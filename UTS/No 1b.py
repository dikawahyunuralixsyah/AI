"MEMPBUAT PROGRAM LIBRARY NUMPY"
import numpy as np
"MENAMBHKANKAN INPUT 10 LAYERS"
inputs = [3.12, 4.13, 2.23, 6.42, 12.3, 4.51, 13.1, 5.6, 9.4, 8.6]
"MENAMBAHKAN WEIGHT 10 ISINYA DAN 5 NEURON"
weights = [[0.7, 0.62, 0.94, 0.32, 0.24, 0.51, 0.36, 0.24, 0.43, 0.8],
		   [0.35, 0.11, 0.72, 0.98, 0.35, 0.63, 0.42, 0.22, 0.67, 0.53],
		   [0.45, 0.67, 0.53, 0.22, 0.64, 0.53, 0.36, 0.37, 0.44, 0.36],
           [0.55, 0.35, 0.65, 0.43, 0.26, 0.13, 0.17, 0.7, 0.5, 0.31],
           [0.45, 0.64, 0.47, 0.43, 0.13, 0.43, 0.72, 0.53, 0.76, 0.89]]
"MENAMBAH BIASES SESUAI DENGAN ISI NEURON"
biases = [7.0, 2.0, 7.5, 6.5, 4.5]
"MEMBUAT PROGRAM OPERASI UNTUK OUPUTS"
layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)