import numpy as np
X=np.array([(1,2,3),(4,5,6)])
Y=np.array([(1,2,3),(4,5,6)])
print(np.vstack((X,Y)))
print(np.hstack((X,Y)))
#  applying all maths functions

Z=np.arange(0,101,10)
print(Z)

print(np.log(Z))
print(np.sin(Z))
print(np.tan(Z))
# https://numpy.org/devdocs/user/quickstart.html