
#
# ages = [12, 11, 34, 56, 55, 88, 89, 56, 74]
#
# def insertionSort(data):
#
#      for i in range(1,len(ages)):
#          key = data[i]
#          j=i-1
#          while j>=0 and data[j]>key:
#              data[j+1]=data[j]
#              j=j-1
#          data[j+1]=key
#      print(ages)
#
# insertionSort(ages)

ages=[20,10,30]
ages1=[]

def insertion(data ,length):
    if length==1:
        return data[0]
    else:

        num=insertion(data,length-1)

        key=data[length-1]

        # data[length-1]=num
        i=length-2
    while(i>=0 and data[i]>key):
            data[i+1]=data[i]
            i=i-1
            data[i+1]=key
    for j in range(len(ages)):
        ages1.append(data[j])
    # print(ages1)
    return ages1

result=insertion(ages,3)
print(result)


# checking python 32 or 64 bit
# import platform
# print(platform.architecture())
#



#
#
# def sort(data,length):
#     if length==1:
#         return data[0]
#     else:
#
#             def sort1():
#                 num = sort(data, length - 1)
#              if num>data[length-1]:
#                 data[0]=data[length-1]
#                 return data[length-1]
# def sort1()
#     else:
#     return data[0]
#
#
# data= [12, 11, 34, 56, 55, 88]
# print("sorted list",sort(data,6))

