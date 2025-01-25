import numpy as np

# Advanced Extra Exercise 1
# Creating a random matrix.
data = np.random.rand(5,5)

# Saving the matrix to 'matrix.txt' in the same directory.
np.savetxt('matrix.txt', data, delimiter =', ')