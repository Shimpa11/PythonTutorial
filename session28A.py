import pandas as pd
import numpy as np

numbers1=[10,20,30,40,50]
numbers2=np.arange(11,51,10)
student={
    "name":"John",
    "age":20,
    "salary":30000
}
series1=pd.Series(numbers1)
print(series1)
print("--------------------")
series2=pd.Series(numbers2)
print(series2)
print("--------------------")
series3=pd.Series(student)
print(series3)
print("_______Accessing data in series--------")
# access the data using indexing

print(series1[2])
print(series2[3])
print(series3["name"])
# Apply Slicing

print("====slicing========")
print(series1[1:3])
print(series2[3:])
print(series3["name":"salary"])
print(series3["name":])
print()
print(series3["age":])

print("Updating data")
series1[1]=111
series2[2]=222
print(series1)
print(series2)

print("Updating data in dictionary")

series3["name"]="Fiona"
print(series3)

print("Delete data")

del series1[0]
print("Appending new data")
series1[5]=55
series1[50]=77 # works as dictionary
# series1.append(77) Error as we cannot append int data into series or only series and frame data
print(series1)

series3["email"]="fiona@example.com"
print(series3)

