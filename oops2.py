
# 1. Think of an Object
#    Customer is Object
#    name, phone, email, gender, address are Attributes

class customer:

    # __init__ : constructor, which gets executed when we create object
    # self is a reference variable, which holds the hashcode of current object
    # name of self can by any name of your choice
    # BUT self is always the first input to __init__

    def __init__(self):
        print("init executed")
        print("self is:",self)
        self.name="john"
cRef1=customer()

print(cRef1.__dict__)

cRef2=customer()
print(cRef2.__dict__)

cRef3=cRef1  # reference copy operation only two objects are  created
# cRef3 will contaion the hashcode of cRef1

print(cRef3.__dict__) # cref not created so init will not execute