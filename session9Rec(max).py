ages = [12, 11, 34, 56, 55, 88, 89, 56, 74]
#
def insertionSort(data):

     for i in range(1,len(ages)):
         key = data[i]
         j=i-1
         while j>=0 and data[j]>key:
             data[j+1]=data[j]
             j=j-1
         data[j+1]=key
     print(ages)

insertionSort(ages)




def maxNumber(data, length):
    if length == 1:
        return data[0]
    else:
        num = maxNumber(data, length-1)

    if num > data[length-1]:
        return num
    else:
        return data[length - 1]



numbers = [10, 20, 30,40]

print(">> max is:", maxNumber(numbers, 4))
