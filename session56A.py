import torch
X=torch.randn(5,5)
print(X)


#  constructing or resizing 2d array is converted into 1d array
Y=X.view(25)
print(Y)

# flattening 2d array into array of 1d array
Z=X.view(-1,25)
print(Z)

print(X.shape)
print(Y.shape)
print(Z.shape)

P=torch.randn(1)
print(P)
# item works whre we have only one value in tensor
print(P.item())