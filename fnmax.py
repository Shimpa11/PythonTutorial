
data =[5,2,6,8,4025,555]
# maximum = data[0]
def myMax():
    maximum=data[0]
    for i in range(0,len(data)):

        if data[i]>maximum:
            maximum=data[i]
    return maximum

print("the maximun of data is:",myMax())
