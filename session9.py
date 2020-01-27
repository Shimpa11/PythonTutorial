ages = [12, 11, 34, 56, 55, 88, 89, 56, 74]

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




