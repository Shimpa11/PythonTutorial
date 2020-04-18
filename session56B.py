"""
Pytorch and numpy
bridging between numpy and pytorch
"""
import torch
import numpy as np

# torch to numpy
X=torch.ones(5)
print(X,type(X))

Y=X.numpy()
print(Y)
print(type(Y))

# adding 1 to elements
X.add_(1)
# Y is also changed as numpy array is being read from tensor itself
print(X)
print(Y)
print()

# numpy totorch
A=np.ones(5)
B=torch.from_numpy(A)
print(A)
print(B)

np.add(A,1,out=A)
print(A)
print(B)

# CUDA api by nvidia
