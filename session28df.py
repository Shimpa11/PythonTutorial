
import pandas as pd
nums1=[10,20,30,40,50]
nums2=[11,22,33,44,55]
emp1={"name":"john","age":22,"salary":30000}
emp2={"name":"Fiona","age":24,"salary":40000}
emp3={"name":"Dave","age":26,"salary":50000}
emp4={"name":"Kia","age":28,"salary":80000 ,"email":"kia@example.com"}
frame1=pd.DataFrame([nums1,nums2])
# passing list in dataframe
frame2=pd.DataFrame([emp1,emp2,emp3,emp4])
print(frame1)
print("=========")
# col indexes are keys and rows indexes are values

print(frame2)

print("Access data in dataframe")
# fetched data col wise
print(frame1[0])
print(frame2["name"])
print(frame1[1][1])
print(frame2["salary"][2])

print("Slicing on data in Dataframe")
print("---------------------")

print(frame1[0:2])
# print(frame1[0:])
# print(frame2["name":"salary"])
print(frame2[0:2])


print("Delete data in dataframe")
# del frame1[0]
# del frame1[1][1]
# print(frame1)


# del a row or column
print("drop")

#  drop-> either  axis=0 for row or axis=1 for column
# frame1.drop(0,axis=0)
frame3=frame1.drop(0,axis=0)
# print(frame1) no change new frame will be generated

print(frame3)
#  or to heve changes in same dataframe
print("change in same data frame")
frame1.drop(0,axis=0,inplace=True)
print(frame1)


# del a value in table

print("Update data in dataframe")
frame1[1]=111
print(frame1)
# frame1[1][1]
# print(frame1)