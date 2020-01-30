class Dish:
    def __init__(self, name, price, description, type):
        self.name = name
        self.price = price
        self.description = description
        self.type = type
        self.quantity = 0

    def showDish(self):
        print("===={}====".format(self.name))
        print("{}\t{}\t{}\t{}".format(self.price, self.description,
                                      self.type, self.quantity))
        print("===========================")


dish1 = Dish("Dal Makhani", 200, "Black Lentils Cooked Overnight", "Indian Veg")
dish2 = Dish("Paneer Makhani", 300, "Makhanwala Paneer", "Indian Veg")
dish3 = Dish("Burger", 100, "Tikkiwala Burger", "Indian Veg")
dish4 = Dish("Noodles", 200, "Desi Noodles", "Desi Chinese")
dish5 = Dish("Manchurian", 150, "Gol Gol Manchurian", "Desi Chinese")


cart=[]
# dish1.quantity=2
# cart.append(dish1)
#
# dish2.quantity=1
# cart.append(dish2)
#
# dish3.quantity=2
# cart.append(dish3)

totalDishes=0
def addDishesToCart(dish):
    global totalDishes
    cart.append(dish)
    totalDishes=totalDishes+1
dish1.quantity=2
dish2.quantity=1
dish3.quantity=2

addDishesToCart(dish1)
addDishesToCart(dish2)
addDishesToCart(dish3)


totalPrice=0
totalItems=0
for dish in cart:
    dish.showDish()
    totalPrice=totalPrice+(dish.price*dish.quantity)
    totalItems=totalItems+dish.quantity

print("the total dishes are:",totalDishes)
print("the total price is:",totalPrice)
print("the total items are:",totalItems)
