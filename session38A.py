from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
# Initial Data
X=[1,2,3,4,5]
Y=[2,4,5,4,5]

data=stats.linregress(X,Y)
print("slope is: ",data[0])
print("Interceptor is: ",data[1])
print("Equation of line: y={}+{}*x".format(data[1],data[0]))

maxX=np.max(X)+10
minY=np.min(Y)-10

print("maxX is: ",maxX)
print("minY is: ",minY)

# data points for linear Regression, 100 data points
x=np.linspace(minY,maxX,100)

y=data[1]+data[0]*x
print(x)
print()
print(y)

plt.plot(x,y,color="m",label="Regression Line")
plt.scatter(X,Y,color="r",label='Data Points')
plt.legend()
plt.show()

