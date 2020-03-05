import  numpy as np
import time
import sys
timeStamp1=time.time()
# print(timeStamp1)

# array1=np.array([10,20,330,40,50])

array1=np.array(list(range(1,1001,1)))
print(array1)

for num in array1:
    print(num)

    # to know time taken to print these numbers

timeStamp2=time.time()
print(timeStamp2-timeStamp1)

numbers=list(range(1,1001))
timeStamp3=time.time()
for num in numbers:
    print(num)

timeStamp4=time.time()
print(timeStamp4-timeStamp3)

# list memory and array memory
S=range(1000)
print(sys.getsizeof(5)*len(S))

D=np.arange(1000)

print(D.size*D.itemsize)



