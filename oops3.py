# 1. Think of an Object
#    Customer is Object
#    name, phone, email, gender, address are Attributes

# 2. Create its Class
class customer:

    # __init__ : constructor, which gets executed when we create object
    #            init can have inputs as many as you want

    # self is a reference variable, which holds the hashcode of current object
    # name of self can by any name of your choice
    # BUT self is always the first input to __init__

    def __init__(self, name, phone, email, gender, address):
        print("init executed")
        print(">> self is:", self)
        # LHS | self.name | is creating attribute in current Object
        # RHS | name      | is input containing data which we assign to attribute
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address
  # OVERLOADING : NOT SUPPORTED
# Creating same __init__ function will create new init and delete old init
        """
        def __init__(self, name, phone, email, gender, address, customerType):
            print("init executed")
            print(">> self is:", self)
            # LHS | self.name | is creating attribute in current Object
            # RHS | name      | is input containing data which we assign to attribute
            self.name = name
            self.phone = phone
            self.email = email
            self.gender = gender
            self.address = address
        """

        # if we create any function in class, its first input is self
    def showCustomerDetails(self):

            # print("the name is {}.the gender is {}".format(self.name, self.gender))
            print(">> {} can be called at {} and lives in {}. For Email {}".format(self.name, self.phone, self.address,
                                                                                   self.email))
    def upgradeToPrime(self,customerType,wallet):
        self.customerType=customerType
        self.wallet=wallet

    def showPrimeCustomer(self,plan):
        self.plan=plan

    def updateCustomerDetails(self,name,phone,email,gender,address):
        self.name=name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address


# creating object from class

cRef1=customer("John","99999 88888", "john@example.com","Male","Redwood")
cRef2=customer("FIonaa","90099 20888","fionaa@example.com","Female","country homes")

# read
print(cRef1.__dict__)
print(cRef2.__dict__)
# update
cRef1.age="20"
print(cRef1.__dict__)



# show customer details
cRef1.showCustomerDetails()
cRef2.showCustomerDetails()

cRef1.upgradeToPrime("prime","100")
print(cRef1.__dict__)


# using update function
cRef2.updateCustomerDetails("fionaa flynn","09080 50555","flynn@example.com","female","countrywood")
print(cRef2.__dict__)

cRef2.showPrimeCustomer("200")
print(cRef2.__dict__)