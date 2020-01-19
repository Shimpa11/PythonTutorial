# amount=int(input("Enter the amount:"))
# minAmount=500
# discount=0.5*amount
# amount=amount-discount
# print("you have got 50% OFF. Please pay:",)



# # regular ifelse
# if amount>minAmount:
#     amount=amount - 0.5 * amount
#     print("you have got 50% OFF. Please pay:", amount)
# else:
#     print("No discount.Pleass add", (minAmount-amount), "to get 50% OFF")



    # ladder ifelse
    #

    # """
    # >200 get 40% off
    # >100 get 50% off upto 150
    # """

amount = int(input("Enter the amount:"))
code=input("Enter Promo Code:")

if amount>200 and code=="zomato":
        amount=amount-0.4*amount
        print(" Promo code applied .You got 40& off. Pay:", amount)


elif amount>100 and code=="offer50":
    discount=0.5*amount
    if discount>150:
        amount=amount-150

    else:
        amount=amount-discount

    print("Promo code offer50 applied .You got 50& off. Pay:", amount)
else:
    print("no discounts. Pay:\u20b9", amount)







