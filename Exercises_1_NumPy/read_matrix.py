import numpy as np

# loads the matrix file, delimited by comma.
data = np.loadtxt("matrix.txt", delimiter = ',')

# changes data to numpy.
print(data)