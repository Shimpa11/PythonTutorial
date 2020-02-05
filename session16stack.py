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

class Stack:
    size=0
    items=0
    price=0

    def __init__(self):
        print("Stack Created")
        print(self)
        self.head=None
        self.current=None

    def push(self,product):
        print(product)
        Stack.size += 1
        Stack.items += product.quantity
        Stack.price += (product.quantity * product.price)

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



    def iterate(self):
        temp=self.current

        while temp.previousProduct!=self.current:
            temp.showProductDetails()
            print("############################")
            temp=temp.previousProduct
        temp.showProductDetails()

    def pop(self):
        self.current=self.current.previousProduct
        self.current.nextProduct=self.head
        self.head.previousProduct=self.current

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

shoppingCart=Stack()
shoppingCart.push(Product(101, "iPhoneX", 70000,1))
shoppingCart.push(Product(301, "AlphaBounce", 8000,2))
shoppingCart.push(Product(701, "Samsung LED", 40000,2))

print("=====================================================")

shoppingCart.iterate()
print("**********************************")

shoppingCart.pop()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
shoppingCart.pop()
shoppingCart.iterate()



