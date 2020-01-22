# student={
#     "name":"John",
#     "email":"John@example.com",
#     "number":101
# }
# print(student)
# # indexs are repleced  by keys and keys are always strings
menu={
    "dal":   200,
    "paneer": 250,
    "naan":   20,
    "salad":  50,
    "noodles": 100,

}
print("Menu for you")
print(menu.keys())
cart=[]
print(cart,type(cart),len(cart))
choice="yes"
while choice=="yes":
    foodItem=input("Enter foodItem:")
    # to select only from menu
    if foodItem in menu:
        cart.append(foodItem)
        choice=input("Would you like to enter more food item(yes/no):")
    else:
        print("select any other fooditem")
print("your cart is:",cart)
#     adding price along with the items
totalPrice=0
for item in cart:
    totalPrice=totalPrice+menu[item]
print("totalPrice is:",totalPrice)

# promocode
promoCode=input("Enter Promo Code:")
if totalPrice>200 and promoCode=="zomato":
    totalPrice=totalPrice-0.4*totalPrice
    print("promocode applied, please pay:", totalPrice)

else:
    print("no discount, please pay:",totalPrice)


# cart.extend(["salad"])
# print("surprise cart:",cart)
#
# cart.insert(1,"champ")
# print("new cart after insert", cart)
#
# cart.pop(2)
# print("cart after pop:",cart)