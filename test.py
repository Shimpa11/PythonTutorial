# from sys import argv
# def print_two(*args):
#     arg1,arg2=args
#     print(f"arg1:{arg1},arg2:{arg2}")
# print_two("John","Wick")

# def foo(num):
#     if (num<=0):
#         return
#     else:
#         print(num/2,end=" ")
#         foo(int(num/2))
#         print(num/2,end=" ")
# foo(20)

x='1'
y=''
# for i in range(0,30):
#     j=0
#     k=0
#     while j< len(x):
#         while k <len(x) and x[k]==x[j]:k+1
#         y+=str(k-j)+x[j]
#         j=k
#     x=y
#     y=''
# print(len(x))
# print(len(y))

import math

x=2**3
y=math.pow(2,3)
print(x)
print(y)

import  os
image_path = os.path.join(os.getcwd(), ('images/'))
print(image_path)