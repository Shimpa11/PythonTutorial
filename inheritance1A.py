
# What is Inheritance ?
# It is a Relationship between 2 classes,
# where child class is allowed to access properties of parent class

class Parent:
# property of class
    vehicle="PB10OA5233"

    def __init__(self,fName,lName):
        # self.fname, self.lname is Property of   Object
        self.fName=fName
        self.lName=lName

# Inheritance
class child(Parent):
    pass
# object of child

cref=child("Fiona", "Flynn")


pref=Parent("Shimpa","Sethi")
print(pref.vehicle)
print(pref.__dict__)
# pref("Parent Dictionary")
print(Parent.__dict__)
print(child.__dict__)
print(cref.__dict__)

print(cref.vehicle)
print(child.vehicle)




