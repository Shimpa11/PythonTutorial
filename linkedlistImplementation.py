class Product:
    def __init__(self,pid,name, price, quantity):
        self.pid=pid
        self.name=name
        self.price=price
        self.quantity=quantity
        self.nextProduct=None
        self.previousProduct=None

    def showProductDetails(self):
        print("@@@{}@@@{}@@@{}@@@".format(self.pid,self.name,self.price))

class linkedList:
    size=0
    items=0
    price=0

    def __init__(self):
        print("Linked List Created")
        print(self)
        self.head=None
        self.current=None

    def append(self,product):
        print(product)

        if self.head ==None:
            self.head=product
            self.current=product
        else:

            product.previousProduct=self.current
            self.current.nextProduct=product

            self.current=product

            product.nextProduct=self.head
            # Fixing 1st Product Object's Previous to be the current for iterating
            # in backward directions

            self.head.previousProduct=self.current

    def iterateForward(self):
        temp=self.head
        while temp.nextProduct!=self.head:
            temp.showProductDetails()
            print("-----------------------")
            temp=temp.nextProduct
        temp.showProductDetails()

    def iterateBackward(self):
        temp=self.current

        while temp.previousProduct!=self.current:
            temp.showProductDetails()
            print("############################")
            temp=temp.previousProduct
        temp.showProductDetails()

    def getTotalPrice(self):
        totalPrice=0
        totalItems=0
        totalProducts=0

        temp=self.head
        while temp.nextProduct!=self.head:

            totalPrice=totalPrice+(temp.price*temp.quantity)
            totalItems=totalItems+temp.quantity
            totalProducts=totalProducts+1
            temp = temp.nextProduct

        totalPrice = totalPrice + (temp.price * temp.quantity)
        totalItems = totalItems + temp.quantity

        totalProducts = totalProducts + 1


        return (totalPrice,totalItems,totalProducts)

    # product1 = Product(101, "iPhoneX", 70000)
    # product2 = Product(301, "AlphaBounce", 8000)
    # product3 = Product(701, "Samsung LED", 40000)
    # shoppingCart.append(product1)
    # shoppingCart.append(product2)
    # shoppingCart.append(product3)

shoppingCart=linkedList()
shoppingCart.append(Product(101, "iPhoneX", 70000,1))
shoppingCart.append(Product(301, "AlphaBounce", 8000,2))
shoppingCart.append(Product(701, "Samsung LED", 40000,2))

shoppingCart.iterateForward()
print("=====================================================")

shoppingCart.iterateBackward()

result=shoppingCart.getTotalPrice()
print("the total price is:",result[0])
print("the total items are:",result[1])
print("the total products are:",result[2])
