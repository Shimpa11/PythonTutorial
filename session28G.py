import numpy as np
import matplotlib.pyplot as plt
A=[1,2,3,4,5]
B=[10,20,30,40,50]
# plt.bar(A,B)


scores={"sachin":200,"Rohit":264,"Virat":183,"Yuvraj":139}
plt.bar(0,scores["sachin"])
plt.bar(1,scores["Rohit"])
plt.bar(2,scores["Virat"])
plt.bar(3,scores["Yuvraj"])

#
# for i, key in enumerate(scores):
#     print(i,key,scores[key])
#     # plt.bar(i,scores[key])
#     plt.bar(key,scores[key])
plt.show()






