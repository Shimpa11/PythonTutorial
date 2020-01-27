
data =[2,5,6,8,55,4506,4000,568,2000]

def myMax():
    for i in range(1,len(data)):
        maximum = data[0]
        if data[i]>maximum:
            maximum=data[i]
    return maximum

print("the maximun of data is:",myMax())
