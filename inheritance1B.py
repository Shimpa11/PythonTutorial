# What is Inheritance ?
# It is a Relationship between 2 classes,
# where child class is allowed to access properties of parent class

class Parent:

    vehicle="PB10AB5233"

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname


    # property of class
    def showParent(self):
         print("{}////{}///{}".format(self.fname,self.lname,Parent.vehicle))


class Child(Parent):
    # vehicle="PB10AA2233"

    def __init__(self, name, salary):
        self.name = name
        self.salary=salary

    def showChild(self):
        print("{}!!!{}!!!".format(self.name,self.salary))


    def show (self,ref):
        print("{}!!!".format(self.ref))
        Parent.showParent(ref)


pRef=Parent("Shimpa","Sethi")
print(Parent.__dict__)
print(Child.__dict__)
print(pRef.__dict__)
pRef.showParent()

cRef=Child("Fionaa","Flynn")
print(cRef.__dict__)
cRef.showChild()  # or

# Child.showChild(cRef)

print(cRef.vehicle)
cRef.show(pRef)

# Lookup Rule:
# If we have not found an attribute in Object, look up for the same in Class
# In Inheritance, lookup shall go upto Parent