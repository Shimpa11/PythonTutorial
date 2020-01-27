data=[0,2,3,55,4,5505,6]
print(len(data))
print((max(data)))


# list comprehension , don't work on expressions

print([x**2 for x in data])
productPrices=[1235,5625,7845]
print([0.4*x for x in productPrices])
# list comprehension , dont work on expressions
# print(x[x-0.4*x for x in productPrices])

# for i in range(0, len(data)):
# print("max:",max(data))

def myMax():
    # if i==max(data):
   return
print("max in function",max(data))
myMax()

def myMin():
    # if i==max(data):
   return
print("min in function",min(data))

myMin()

maximum=data[0]
for i in range(1,len(data)):
    print(data[i])
    if data[i]>maximum:
        maximum=data[i]
print("got the max number:",maximum)

# min value
minimum=data[0]
for i in range(1,len(data)):
    print(data[i])
    if data[i]<minimum:
        minimum=data[i]
print("got the min number:",minimum)











