import numpy as np

arr = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])

# Slicing the first two rows and columns
sliced_arr = arr[:2, :2]  # Output: [[1, 2], [4, 5]]
print("Sliced Array:\n", sliced_arr)

# Create an array
arr1 = np.array([1, 2, 3, 4, 5, 6])

# Conditional slicing: select elements greater than 3
conditional_slice = arr1[arr1 > 3]  # Output: [4, 5, 6]
print(arr[arr>2])
print("Conditional Slice:\n", conditional_slice)


arr = np.array([1, 2, 3, 4])

# Applying mathematical functions
squared = np.square(arr)        # Output: [ 1,  4,  9, 16]
sqrt = np.sqrt(arr)            # Output: [1.         1.41421356 1.73205081 2.        ]
mean=np.mean(arr)
print("Mean :\n",mean)
print("Squared:\n", squared)
print("Square Root:\n", sqrt)

# Using lists
list_arr = [1, 2, 3, 4]

# Squaring each element using list comprehension
squared_list = [x**2 for x in list_arr]  # Output: [1, 4, 9, 16]

print("Squared List:\n", squared_list)

# Squared using NumPy (faster and more concise)
squared_np = np.square(np.array(list_arr))  # Output: [ 1,  4,  9, 16]
print("Squared NumPy Array:\n", squared_np)

# Define a custom function
def custom_func(x):
    return x ** 2 + 2 * x + 1  # (x + 1) ** 2

# Apply custom function using np.vectorize
vectorized_func = np.vectorize(custom_func)
result = vectorized_func(arr)  # Apply to NumPy array

print("Result of Custom Function:\n", result)

# sum
s=np.sum(arr)
print("sum is :",s)

# product
s=np.prod(arr)
print("product is :",s)

# median
s=np.median(arr)
print("median is :",s)

# min
s=np.min(arr)
print("min is :",s)

# max
s=np.max(arr)
print("max is :",s)

# std deviation
s=np.std(arr)
print("std is :",s)

# variance
s=np.var(arr)
print("var is :",s)

# element wise 
# add
s=np.add(arr,5)
print("new array  is :",s)

# subtract
s=np.subtract(arr,-2)
print("new array after subtract is :",s)

# multiply
s=np.multiply(arr,-3)
print("new array after multiply is :",s)

# divide
s=np.divide(arr,2)
print("new array after divide is :",s)

# power
s=np.power(arr,4)
print("new array after power is :",s)


'''
output
Sliced Array:
 [[1 2]
 [4 5]]
[3 4 5 6 7 8 9]
Conditional Slice:
 [4 5 6]
Mean :
 2.5
Squared:
 [ 1  4  9 16]
Square Root:
 [1.         1.41421356 1.73205081 2.        ]
Squared List:
 [1, 4, 9, 16]
Squared NumPy Array:
 [ 1  4  9 16]
Result of Custom Function:
 [ 4  9 16 25]
sum is : 10
product is : 24
median is : 2.5
min is : 1
max is : 4
std is : 1.118033988749895
var is : 1.25
new array  is : [6 7 8 9]
new array after subtract is : [3 4 5 6]
new array after multiply is : [ -3  -6  -9 -12]
new array after divide is : [0.5 1.  1.5 2. ]
new array after power is : [  1  16  81 256]
'''