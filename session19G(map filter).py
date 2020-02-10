def squareOfNumber(num=1):
    return num*num
lRef1=lambda num: num*num
lRef2=lambda num:num-(num*0.4)
numbers=[10,20,30,40,50,60]
for number in numbers:
    print(lRef1(number))

result=map(squareOfNumber,numbers)
print(result,type(result))
# result=list(map(squareOfNumber,numbers))
# result=list((lRef1,numbers))
# result=list(map(lambda num: num*num,numbers))
# result=list(map(lRef2,numbers))
# result=list(map(lambda num:num-(num*0.4),numbers))
# print(result)


# L1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
L1=list(range(10,21,1))
print(L1)

lRef3=lambda num:num%2==0
lRef4=lambda num:num%2!=0
result=list(map(lRef3,L1))
result1=list(map(lRef4,L1))
result2=list(filter(lRef3,L1))
result3=list(filter(lRef4,L1))
print(result2)
print(result)
print(result1)
print(result3)

lRef5=lambda X,Y:X+Y
L2=[10,20,30,40,50]


from functools import reduce
# result=reduce(lRef5,L2)

# result=reduce(lambda X,Y:X+Y,L2)
result=reduce(lambda X,Y:X+Y,[10,20,30,40,50,60])
print(result)