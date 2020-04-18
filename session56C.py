"""
CUDA
https://www.google.com/search?q=cuda+nvidia

"""
# check if device supports  CUDA
import torch

# if GPU support is available
print(torch.cuda.is_available())

# if available
device=torch.device("cuda")

X=torch.ones(5)
# use GPU capabilities to process the data
Y=torch.ones_like(X,device=device)