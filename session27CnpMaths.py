#Array Maths
import numpy as np
data=[
    (8,9),(10,12),(13,14)
]
arr1=np.array(data)
print(arr1)
print(arr1[0:2, 1])

print(arr1.min())
print(arr1.max())
print(arr1.sum())

#  sum of columns
print(arr1.sum(axis=0))

# sum of rows
print(arr1.sum(axis=1))
# max of axis 1
print(arr1.max(axis=1))
print(arr1.min(axis=0))

print(np.sqrt(arr1))
print(np.std(arr1))

a1=np.array([(1,2,3),(3,4,5)])
a2=np.array([(1,2,3),(3,4,5)])
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2) #  floating point division
print(a1//a2)  # true or integral div

# a3 would be new array , a1 and a2 would not be changed
a3=a1+a2
a3=np.add(a1,a2)
print(a3)
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])

# matrix multiplication
z=np.dot(x,y)
print(z)
print("===Dot product on 1D array")
u=np.array([1,2])
v=np.array([5,6])
w=np.dot(u,v)
print(w)

# transpose
print(x.T)

