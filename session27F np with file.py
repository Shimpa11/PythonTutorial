import numpy as np

# reading data from file
array=np.loadtxt("data.txt",dtype=np.int)
print(array)

arr1D=np.arange(10,200,10)
print(arr1D)
#  saving data in file
np.savetxt("arrayData.txt",arr1D)
#  formatted data
np.savetxt("arrayData1.txt" ,arr1D, fmt="%04d")
print("Data Saved")