"""
1.Think of an object
customer : name age address,phone  gender

"""
# 2.create a class (drawing of an object)


class Customer:
    pass

#3 create real objects from the class

cRef1 = Customer()     #object creation statement

cRef1.name = "john"    # name phone are the attributes and john ,20, male is the data
cRef1.phone = "99999 88888"
cRef1.age = "20"
cRef1.gender = "Male"

print("the cRef is:", cRef1)
print("the type of cref is:", type(cRef1))
print("the id of  cref is:", hex(id(cRef1)))
print(cRef1.__dict__)


#update data in object
cRef1.name="fionaa"
print(cRef1.__dict__)
# add data in object

cRef1.address="Country Homes"
print(cRef1.__dict__)

#del data in object
del cRef1.phone
print(cRef1.__dict__)

# del ref variable pointing to the object created  taken as object

# del cRef1
# print(cRef1.__dict__) error

cRef2=  Customer()
cRef2.name="tim"
cRef2.age="20"
print(cRef2.__dict__)
# read data from the object

print(cRef2.__dict__)

# For End User : How we must show data
print("the name is {}. the age  of {} is {}".format(cRef1.name, cRef1.name,cRef1.age))
print("the name is {}. the age  of {} is {}".format(cRef2.name, cRef2.name,cRef2.age))
