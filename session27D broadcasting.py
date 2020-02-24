"""
BROADCASTING
Working with arrays of different sizes or shape
"""
import  numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("x is")
print(x.shape)

print()
v=np.array([1,0,1])
print("v is:")
print(v.shape)
#  create an empty array of same shape with some garbage data or values
y=np.empty_like(x)
print("y is:")
print(y.shape)

# print("!!!!!!!!!")

for i in range(4):
    y[i,:]=x[i,:]+v
print(y)