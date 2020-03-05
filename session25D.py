"""
n-Queen problem
1.create chess board

take input from user((2x2),4x4,8x8,16x16.......)
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
2. Take input from user to place n-queens

"""

import numpy as np
# array=np.array([[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]]*4)
#
# print(array)

import math
size=int(input("enter the size of board:"))


for i in range(0,5):
     if size == math.pow(2, i):
         for r in range(size):
             for c in range(size):
                 b=(int((r+c+1)%2))
                 # print(int((r + c + 1) % 2),end="")
                 print(b ,end="")
             print()

     # else:
     #    print("enter valid number")

m=np.matrix(b)
print(m)
nQueen=int(input("Enter the number of queens to be placed"))


def placeQueen(num):
    k=1

