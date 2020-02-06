class Customer:
    def __init__(self, name, email, phone):
        self.name=name
        self.email=email
        self.phone=phone


    def showCustomer(self):
        print("CUSTOMER:{}!!!{}!!!{}".format(self.name,self.email,self.phone))

class Burger:
    def __init__(self, type,price,quantity):
        self.type=type
        self.price=price
        self.quantity=quantity

    def showBurger(self):
        print("BURGER:{}!!!{}!!{}".format(self.type,self.price,self.quantity))

burger1=Burger("Cheese burger",150,"1")
burger2=Burger("McBurger",200,"2")
# burger3=Burger("NoodlesBurger",100,"1")
# print()
# burger1.showBurger()
# burger2.showBurger()
# burger3.showBurger()

totalBurgers=0
cart=[]

def addBurgers(burger):
    global totalBurgers
    cart.append(burger)
    totalBurgers = totalBurgers + 1

burger1.quantity = 1
burger2.quantity = 2

addBurgers(burger1)
addBurgers(burger2)
totalPrice = 0
for burger in cart:
    burger.showBurger()

    totalPrice = totalPrice + (burger.quantity * burger.price)
print("Total price is:",totalPrice)
print("Number of burgers",totalBurgers)



class PrimeMeal(Burger):
    mealCombo=200
    def upgradeToPrime(self):
        self.meal=True
        self.coke=True
        self.fries=True

    def showPrimeMeal(self):
        self.showBurger()

        BurgerDetails=self.__dict__
        keys=BurgerDetails.keys()


        if "meal" in keys:

             print("Meal:{} !!{}!!{}".format(self.meal,self.coke,self.fries))


cRef1=Customer("Fiona","fiona@example.com", "91 99889 88998")
print(burger1.__dict__)
PrimeMeal.upgradeToPrime(burger1)


print(burger1.__dict__)
PrimeMeal.showPrimeMeal(burger1)

print("now the total price is",totalPrice+PrimeMeal.mealCombo)



#
# cRef1.showCustomer
# print(cRef1.__dict__)
#
# PrimeCustomer.upgradeToPrime(cRef1)
# print(cRef1.__dict__)
#
# PrimeCustomer.showPrimeCustomer(cRef1)







