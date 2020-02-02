# """
# # Why Inheritance
# # 1. Code ReUsability
# # 2. Only write additional details in Children
# # 3. Saves TIME [DEVELOPMENT] :)
#
# # Inheritance leads to Generalization | IS-A Relationship
# """
#
# class Shoe:
#     def __init__(self,pid,name,price,brand,shoesize):
#         self.pid=pid
#         self.name=name
#         self.price=price
#         self.brand=brand
#         self.shoesize=shoesize
#
#     def showShoeDetails(self):
#         print("======{} | {}======".format(self.pid, self.name))
#         print("{} | {} | {}".format(self.price, self.brand, self.shoeSize))
#         print("===========================")
#
#
# class Mobile:
#     def __init__(self,pid,name,price,brand,ram,os):
#         self.pid=pid
#         self.name=name
#         self.price=price
#         self.brand=brand
#         self.ram=ram
#         self.os=os
#
#     def showMobileDetails(self):
#         print("======{} | {}======".format(self.pid, self.name))
#         print("{} | {} | {}|{}".format(self.price, self.brand, self.ram,self.os))
#         print("===========================")
#
#
# class LEDTV:
#     def __init__(self,pid,name,price,brand, screensize,technology):
#         self.pid=pid
#         self.name=name
#         self.price=price
#         self.brand=brand
#         self.screensize=screensize
#         self.technology=technology
#
#     def showLEDTVDetails(self):
#         print("======{} | {}======".format(self.pid, self.name))
#         print("{} | {}".format(self.price, self.brand))
#         print("{} | {} ".format(self.screensize, self.technology))
#         print("===========================")



class Product:
    def __init__(self,pid,name,price,brand):
            self.pid = pid
            self.name=name
            self.price=price
            self.brand=brand

    def showProductDetails(self):
        print("======{} | {}======".format(self.pid, self.name))
        print("{} | {}".format(self.price, self.brand))

# Shoe IS-A Product
class Shoe(Product):
    def __init__(self, pid, name, price, brand, shoeSize):
        Product.__init__(self, pid, name, price, brand)
        self.shoeSize = shoeSize

    def showShoeDetails(self):
        Product.showProductDetails(self)
        print("{}".format(self.shoeSize))
        print("===========================")
# MobilePhone IS-A Product
class Mobile(Product):
    def __init__(self,pid,name,price,brand,ram,os):
        Product.__init__(self,pid,name,price,brand)
        self.ram=ram
        self.os=os
    def showMobileDetails(self):
        Product.showProductDetails(self)
        print("{} | {} ".format( self.ram, self.os))
        print("===========================")


class LEDTV(Product):
    def __init__(self, pid, name, price, brand,screensize,technology):
        Product.__init__(self, pid, name, price, brand)
        self.screensize = screensize
        self.technology=technology

    def showLEDTVDetails(self):
        Product.showProductDetails(self)
        print("{} | {} ".format(self.screensize, self.technology))
        print("===========================")





sRef=Shoe(101, "AlphaBounce", 8000, "Adidas", 8)
mRef = Mobile(201, "iPhoneX", 70000, "Apple", 4, "iOS")
lRef = LEDTV(301, "Samsung Curved", 50000, "Samsung", 50, "OLED")

sRef.showShoeDetails()
mRef.showMobileDetails()
lRef.showLEDTVDetails()
