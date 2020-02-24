import numpy as np
array=np.arange(10,51,2)

slices=slice(1,20,2)
#  with traditional list and range
indexes=list(range(1,20,2))
print(array)
print(slices)

# filtered data   to get what indexes we want from array or fetching based on indexes
#
print(array[slices])
print(array[indexes])

