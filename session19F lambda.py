#Below func is  single  expression computation
def areaOfCircle(radius=1.0):
    area=3.14*radius*radius
    return  area

A=areaOfCircle(5)
print(A)
#Reference copy operation
area=areaOfCircle
print("Area of circle is",areaOfCircle(5))
print("Area is: ",area(5))
# In mathematics, Lambda compute single expression statements

lRef1=lambda radius=5:3.14*radius*radius
lRef2=lambda x,y: x**y
lRef3=lambda x=int(input("Enter X value: ")),y=int(input("Enter Y value: ")): x**y
lRef4=lambda x=int(input("Enter X value: ")),y=int(input("Enter Y value")): lRef2(x,y)+lRef3(x,y)

print("lRef1 is",lRef1)
print("lRef1 with radius 5: ",lRef1(5))
print("lRef2 with x and y inputs:",lRef2(2,3))
print("lRef3 with x and y inputs:",lRef3(2,3))
print("2 power 9 is:",lRef2(2,9))
print("lRef4 is:",lRef4())

