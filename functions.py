#
# def add(a,b):
#     c=a+b
#     return c
#
# a=int(input("enter num1:"))
# b=int(input("enter num2:"))
#
#
# print(add(a,b))




amount = int(input("Enter the amount:"))
code=input("Enter Promo Code:")

def myFun(amount, code):
    if amount>200 and code=="zomato":
        amount=amount-0.4*amount
        print("please pay:",amount)
    else:
        print("no discounts")
myFun(amount,code)

# if amount>100 and code==JUMBO:
#     discount=amount-0.5*amount
#     if discount>150:
#         amount=amount-150
#         print("pay",amount)
#     else:
#         print("no discount")
# myFun(amount,code)



# print ("please pay:", myFun(amount,"zomato"))



