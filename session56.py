import torch
print(torch.__version__)
# Always explore documentation for your learning part :)
# https://pytorch.org/tutorials/
#  numpy,tf , pytorch focusses on tensors-> nd array
A=torch.rand(5,3)
print(A)
print(type(A))

B=torch.empty(5,3)
print(B)

print()

C=torch.zeros(5,3,dtype=torch.long)
# C=torch.zeros(5,3,dtype=torch.int)
print(C)

print()
D=torch.tensor([10,20,30,40,50])
print(D)

# constructed array of ones from existing array by manipulatingthe data in it
D=D.new_ones(5,3,dtype=torch.double)
print(D)
# E=torch.rand_like(D,dtype=torch.float)
E=torch.randn_like(D,dtype=torch.float)
print(E)


print(E.size())
print(E.shape)

F=torch.rand(5,3)
# use operators to perform matrix operations
print(E+F)
print(torch.add(E,F))

result=torch.empty(5,3)
torch.add(E,F,out=result)
print(result)
print()

#  add E to F and and modify data in F
F.add(E)
print("====Tensor F=====")
print(F)
print()
# Indexing on tensors
print(F[:,1]) # Ist col in tensor