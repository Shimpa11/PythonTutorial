# import matplotlib as plt

import matplotlib.pyplot as plt

"""
# X-axis will be indexes by default
Y=[1,2,3,4,5]
plt.plot(Y)
plt.show()

"""
X=list(range(1,11))
# list comprehension
Y1=[n for n in X]
Y2=[n*n for n in X]
Y3=[n*n*n for n in X]

plt.plot(X,Y1,label="Y1")
plt.plot(X,Y2,label="Y2")
plt.plot(X,Y3,label="Y3")

plt.legend()

plt.title("Polynomial Graphs")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.grid(True)
plt.savefig("MyGraph")

plt.xlim(0,10)
plt.ylim(0,10)

plt.show()







