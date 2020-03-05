
"""
#  Assignment:
data Analysis

# Results:
# 1. How Many Years ?
# 2. Find the City with min temp and max temp
# 3. Find the City with min temp and max temp with Month and Year
# 4. Sort the Months as per temp, city wise | 3 different lists may be thr
# 5. Take and DataSet i.e. CSV file from Kaggle and Analyse the same fo max min avg etc..

"""
import numpy as np
array=np.genfromtxt("cityTemps.csv",delimiter=",")
print(array)
# print(array.shape)


# print(array[1:len(array),0:1])

# print()
# c=0
#
for k in range(1,len(array)+1):
    a=array[:k,:1]
    col3=array[:k,1:]
    # c = c + 1
# print(a)
print(col3)
# print("===max is====")
# print(col3.max())
# print("====min is===")
# print(col3.min())
#
# print("the total number of years:",c)
#
# u=np.unique(a)
# print(u)
# print(u.size)

r=col3.shape[0]
c=col3.shape[1]

# print("the col3 shape is: ",r)
print("========")


for x in col3:
    maximum=col3[0]
    if x >maximum:
        maximum=x
        print("the max value is:", maximum)


#         if col3[i][j] < min:
#              min=col3[i][j]
# # print("the min is:",min)













