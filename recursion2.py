def maxNumber(data, length):
    if length==1:
        return data[0]

    else:
        num=maxNumber(data,length-1)
    if num>data[length-1]:
        return num
    else:
        return data[length-1]

data=[10,20,30,50,40,60]
print("the max number is:",maxNumber(data,6))