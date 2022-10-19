"MEMBUAT PROGRAM DENGAN LIBRABRY NUMPY"
import numpy as np
"MENAMBHKAN INPUT 10 LAYER"
inputs = [20.5, 18.4, 21.8, 14.8, 17.3, 21.3, 19.8, 16.4, 7.0, 20.0]
"MENAMBHKAN WEIGHT 1 NEURON 10 LAYERS"
weights = [0.36, 0.34, 0.56, 0.2, 0.21, 0.1, 0.5, 0.3, 0.4, 0.22]
"MENAMBHKAN BIAS SESUAI DENGAN NEURON"
bias = 6.0
outputs = np.dot(weights, inputs) + bias
print(outputs)