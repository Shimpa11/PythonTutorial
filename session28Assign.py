import numpy as np
import pandas as pd

# array=np.genfromtxt("cityTemps.csv",delimiter=",",skip_header=1)
array=np.genfromtxt("cityTemps.csv",delimiter=",")

# print(array)

u=array[ : ,2]
print(u)
# print(array["Amritsar"])
# print(array["Chandigarh"])

max = u[1]
for x in u:
    if x > max:
        max=x

print("the max is value is:" ,max)

min=u[1]
for g in u:
    if g<min:
        min=g
print("the min value is:",min)



k=array[ 1: ,2:5]
print(k)
# print(k.max())

max=k[0,0]
# for i in np.nditer(k):
#     print(i)
#     print(k[i])


for i in np.arange(np.size(k,0)):
    for j in np.arange(np.size(k,1)):
        if k[i,j]>max:
            max=k[i,j]
print(max)


min=k[0,0]
for i in np.arange(np.size(k,0)):
    for j in np.arange(np.size(k,1)):
        if k[i,j]<min:
            min=k[i,j]
print(min)




print(max)

