import numpy as np
array1=np.ones(8)
array2=np.zeros(8)

print(array1)  #floating point numbers 1.1.
print(array2) # 0.0.

print(array1.shape[0]) # length of nd array, tales less time as com to len func
print(array2.shape)

#print(len(array1)) would take  more time

# reshape the array  in any format but with even shape
array=array1.reshape(2,2,2)
print(array)
#array=array1.reshape(2,2)# error

array=array1.reshape(2,4) # product is number of elements
print(array)
# converting back to original array using ravel function
originalArray=array.ravel()
print(originalArray)

# explore : reshape function

