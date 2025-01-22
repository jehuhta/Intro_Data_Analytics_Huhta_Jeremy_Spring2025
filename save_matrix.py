import numpy as np

# Advanced Extra Exercise 1
# Creating a random matrix.
data = np.random.rand(5,5)

# Saving the data set to a text format.
np.savetxt('data.txt', data, delimiter =', ')