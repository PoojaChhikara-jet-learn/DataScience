import numpy as np

# Explain the difference between lists and arrays

sample_list = [1,2,3,4]
print(type(sample_list))

sample_numpy_array = np.array(sample_list)
print(type(sample_numpy_array))
# error_array = np.array([1,2,3],11)  
#This line will throw an error, arrays are created out of single data-type only

# Create a numpy array of zeroes
array = np.zeros(5)

print(array)

# Create a numpy array of ones
ones_array = np.ones(5)
print(ones_array)

# Specifying the data type during instatiation
float_array = np.array([1,2,3,4,5], dtype = 'f')
print(float_array)

# Create a multi-dimensional array
twod_array = np.array([[1,2], [3,4]])
print(twod_array)

twod_array_error = np.array([[1,2], [3]]) # The rows should have same columns - Error 
# print(twod_array_error)

# Print the dimensions of the array
print(towd_array.ndim)

# Print the shape of the array
print(twod_array.shape()) # It is a tuple, rows and columsn could be accessed independently

# Print the number of elements in the array
print(twod_array.size())

# Print the memory occupied by the array
print(towd_array.nbytes)

# Get an array of numbers from 1 - 100
num_array = np.arange(1, 100)
print(num_array)

# Get an array of numbers from 1-100 for even numbers only
even_array = np.arange(1, 100, 2)
print(even_array)

# Get a random arrangement of numbers
random_arr = np.random.permutation(np.arange(1,10)) # Repeat this line to get different arrangements
print(random_arr) 

# Get a random number using numpy 
random_num = np.random.randint(1,10)
print(random_num)

# Get the random numpy array of specified dimension
random_array = np.random.rand(2,3)
print(random_array)
print(random_array.shape)

# Reshape a linear array to required dimension
reshaped_array = np.arange(1, 10).reshape(3,3)
print(reshaped_array)
print(reshaped_array.shape)

# Exercise - Take a linear array of elements (36) and show the multi-dimensional matrices of possible shapes

linear_array = np.arange(1,37)

print(linear_array.reshape(6,6))
print(linear_array.reshape(12, 3))
print(linear_array.reshape(18,2))


# Show the sorting functionality
random_array = np.random.permutation(np.arange(1,10))
print(random_array)
sorted_array = np.sort(random_array)
print(sorted_array)

