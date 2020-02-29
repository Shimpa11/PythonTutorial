import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# X=np.random.randn(50)
# print(X)

# plt.hist(X,50)
#
# plt.show()
array=np.genfromtxt("cityTemps.csv",delimiter=",")
# print(array)
X=array[1:, 2:5]
print(X)

frame1=pd.DataFrame(X)
print(frame1)



X1=frame1[0]
y1=X1.max()
print("the max temp in ludhiana:",y1)

y4=X1.min()
print("the min temp in ludhiana:",y4)


X2=frame1[1]
y2=X2.max()
print("the max temp in Amritsar:",y2)

y5=X2.min()
print("the min temp in Amritsar:",y5)

X3=frame1[2]
y3=X3.max()
print("the max temp in Chandigarh:",y3)

y6=X3.min()
print("the min temp in Chandigarh:",y6)

maxTemp={"Ludhiana":y1, "Amritsar":y2,"Chandigarh":y3}
minTemp={"Ludhiana":y4, "Amritsar":y5,"Chandigarh":y6}

#
# plt.plot(X1,label="Ludhiana")
# plt.plot(X2,label="Amritsar")
# plt.plot(X3,label="Chandigarh")
#
# plt.legend()

for i,key in enumerate(maxTemp):
    print(i, key, maxTemp[key])
    plt.bar(i+0.5,maxTemp[key],width=0.5,color='r',label="Maximun")

for i,key in enumerate(minTemp):
    print(i,minTemp[key])
    plt.bar(i,minTemp[key],width=0.5,color='g',label="Minimum" )
plt.legend(loc=1)
plt.show()

