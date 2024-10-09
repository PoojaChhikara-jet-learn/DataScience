import numpy as np

# Create a list of numbers
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)
print(type(my_list))

# create array using range (nt converted) 
# Create an array using arange
array_arange = np.arange(1, 11)  # Numbers from 1 to 10
print("Array using arange:", array_arange)

# Reshape to a 2D array (2 rows, 5 columns)
reshaped_array = array_arange.reshape((2, 5))
print("Reshaped Array:\n", reshaped_array)

# Get the shape of the reshaped array
shape_of_array = reshaped_array.shape
print("Shape of Reshaped Array:", shape_of_array)  # Output: (2, 5)



# Convert list to NumPy array
my_array = np.array(my_list)
print("NumPy Array:", my_array)

# basic +/-/*/% etc operations in all 
added_array = my_array + 5
print("Array after adding 5:", added_array)  # Output: [15 25 35 45 55]

multiplied_array = my_array * 2
print("Array after multiplying by 2:", multiplied_array)  # Output: [20 40 60 80 100]

# Slice the first three elements
sliced_array = my_array[:3]
print("Sliced Array (first 3 elements):", sliced_array)  # Output: [10 20 30]
print(my_array[1:])
print(my_array[2:4])
print(my_array[::4]) #: first indicates that we need all from start to end and : 2nd indicates jump

# sorting the array(In NumPy, the numpy.sort() function uses different 
# sorting algorithms depending on the type of sort you specify with the kind 
# parameter. By default, NumPy uses Quicksort, but other options are available as well.)
sorted_array = np.sort(my_array)
print("Sorted Array:", sorted_array)  # Output: [10 20 30 40 50]


# mean and sum of array
mean_value = np.mean(my_array)
sum_value = np.sum(my_array)
print("Mean:", mean_value)  # Output: 30.0
print("Sum:", sum_value)    # Output: 150



# lets make 2d array 
# reshaping the array
reshaped_array = my_array.reshape((5, 1))
print("Reshaped Array:\n", reshaped_array)

# filtered array
filtered_array = my_array[my_array > 25]
print("Filtered Array (elements > 25):", filtered_array)  # Output: [30 40 50]


# find the indices 
sorted_indices = np.argsort(my_array)
print("Indices of Sorted Array:", sorted_indices)  # Output: [0 1 2 3 4]


# sum and mean for 2d array
# Create a 2D array from existing list /array
my_2d_array = my_array.reshape((1, 5))
print("2D Array:\n", my_2d_array)

# Sum along the first axis (rows)
sum_along_axis = np.sum(my_2d_array, axis=1)
print("Sum along axis 1:", sum_along_axis)  # Output: [150]


# Create a 3x3 array of zeros
array_zeros = np.zeros((3, 3))
print("Array of Zeros:\n", array_zeros)

# Create a 2x4 array of ones
array_ones = np.ones((2, 4))
print("Array of Ones:\n", array_ones)

# Create an empty array of shape (2, 3)
array_empty = np.empty((2, 3))
print("Empty Array:\n", array_empty)


# Using eye
identity_matrix = np.eye(4)
print("Identity Matrix:\n", identity_matrix)
# or
import numpy as np

# Create a 4x4 identity matrix
identity_matrix = np.identity(4)
print("Identity Matrix using np.identity:\n", identity_matrix)

# or
# Create a 4x4 identity matrix using np.diag
identity_matrix_diag = np.diag(np.ones(4))
print("Identity Matrix using np.diag:\n", identity_matrix_diag)

# 
# Create a 4x4 zero matrix
zero_matrix = np.zeros((4, 4))

# Fill the diagonal with ones or any value
np.fill_diagonal(zero_matrix, 5)
print("Identity Matrix using np.fill_diagonal:\n", zero_matrix)


# Create a NumPy array
arr = np.array([1, 2, 3])

# Append a single value
new_arr = np.append(arr, 4)
print("Array after appending 4:", new_arr)  # Output: [1 2 3 4]

# Append multiple values
new_arr_multiple = np.append(arr, [5, 6, 7])
print("Array after appending [5, 6, 7]:", new_arr_multiple)  # Output: [1 2 3 5 6 7]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate two arrays
concatenated_arr = np.concatenate((arr1, arr2))
print("Concatenated Array:", concatenated_arr)  # Output: [1 2 3 4 5 6]

# stacking arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

# Vertical stack
vstacked_arr = np.vstack((arr1, arr2))
print("Vertically Stacked Array:\n", vstacked_arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# Horizontal stack
hstacked_arr = np.hstack((arr1, arr2.T))  # Transpose arr2 to match dimensions
print("Horizontally Stacked Array:\n", hstacked_arr)
# Output:
# [[1 2 5]
#  [3 4 6]]

arr = np.array([1, 2, 3, 4, 5])

# Remove the element at index 2
new_arr = np.delete(arr, 2)
print("Array after deleting index 2:", new_arr)  # Output: [1 2 4 5]

# Remove multiple elements (e.g., indices 1 and 3)
new_arr_multiple = np.delete(arr, [1, 3])
print("Array after deleting indices 1 and 3:", new_arr_multiple)  # Output: [1 3 5]

arr = np.array([1, 2, 3, 4, 5])

# Remove all elements greater than 3
filtered_arr = arr[arr <= 3]
print("Array after removing elements > 3:", filtered_arr)  # Output: [1 2 3]
