amount = int(input("Enter the amount:"))
code=input("Enter Promo Code:")

# if amount>200:
#     if code=="zomato":
#         amount=amount-0.4*amount
#         print("pay", amount)
#     else:
#         print("try code zomato to get 40% OFF")
#
# elif amount>100:
#     if code == "JUMBO":
#         discount = 0.5 * amount
#         if discount > 150:
#             amount = amount - 150
#         else:
#             amount = amount - discount
#         print(">> JUMBO Applied Successfully !! 50% OFF upto 150")
#         print(">> Please Pay: \u20b9", amount)
#     else:
#         print(">> Try using JUMBO to get 50% OFF")
# else:
#     print(">> Please Pay: \u20b9", amount)

if amount>100:
        if code=="JUMBO":
            discount = 0.5 * amount
            if discount > 150:
                amount = amount - 150
            else:
                amount = amount - discount
                print("pay \u20b9", amount)

            print("got 50%Off")

        elif code=="zomato" and amount>200:
            amount = amount - 0.4 * amount
            print("pay:\u20b9", amount)
            print("try using JUMBO to get 50% off")
else:
        print("pay \u20b9",amount)










