
# optimised -> better on memory and time while usage :)
# numpy array is optimised as compared to the list :)
import numpy as np
numbers=[10,20,30,40,50]
print(numbers, type(numbers))

print()
#with list
array=np.array(numbers)

# array=np.array([10,20,30,40,50])
print(array, type(array)) # numpy's n -dimensional array arrays are faster than list, to fetch, optimized as compared to the list


# with tuple
array1=np.array((10,20,30,40,50))
print(array1,type(array1))

# with set
array2=np.array({10,20,30,40,50})
print(array2,type(array2))

#array with single element of string type
array3=np.array("Hello")
#array3=np.array("Hello", ""Hi") Error
print(array3, type(array3))

array4=np.array([{"name":"John","age":30},{"name":"Fiona","age":22}])
print(array4,type(array4))


# array with one single element
array5=np.array(30)
print(array5,type(array5))

#updating data in array
array[2]=222
print(array)

# iterate in array
for num in array:
    print(num)

for data in array4:
    print(data)
print()
#this is immutable operattion, new array will be created
array=np.append(array1,[11,22,33,44,55])
print(array1)
print(array)


