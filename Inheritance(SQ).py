class Product:
        def __init__(self, pid, name, price, quantity):
            self.pid = pid
            self.name = name
            self.price = price
            self.quantity = quantity
            self.nextProduct = None
            self.previousProduct = None

        def showProductDetails(self):
            print("@@@{}@@@{}@@@{}@@@".format(self.pid, self.name, self.price))

class LinkedList:
        def __init__(self):
            # print("Linked List Created")
            print(self)
            self.head = None
            self.current = None

        def append(self, product):
            print(product)

            if self.head == None:
                self.head = product
                self.current = product
            else:

                product.previousProduct = self.current
                self.current.nextProduct = product

                self.current = product

                product.nextProduct = self.head
                # Fixing 1st Product Object's Previous to be the current for iterating
                # in backward directions

                self.head.previousProduct = self.current

        def iterateForward(self):
            temp = self.head
            while temp.nextProduct != self.head:
                temp.showProductDetails()
                print("-----------------------")
                temp = temp.nextProduct
            temp.showProductDetails()

        def iterateBackward(self):
            temp = self.current

            while temp.previousProduct != self.current:
                temp.showProductDetails()
                print("---------------------------------------")
                temp = temp.previousProduct
            temp.showProductDetails()

class Stack(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        print("Stack Created")

    def showStack(self):
        self.nextProduct = None
        self.previousProduct = None

    def push (self,product):
        self.append(product)

    def pop(self):
        self.current = self.current.previousProduct
        self.current.nextProduct = self.head
        self.head.previousProduct = self.current


class Queue(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        print("Queue Created")
    def showQueue(self):
        self.nextProduct = None
        self.previousProduct = None

    def add(self,product):
        self.append(product)


    def poll(self):
        self.head = self.head.nextProduct
        self.head.prevProduct = self.current
        self.current.nextProduct = self.head

    def peek(self):
        self.head.showProductDetails()


shoppingCart = LinkedList()
shoppingCart= Stack()

shoppingCart.append(Product(101, "iPhoneX", 70000, 1))
shoppingCart.append(Product(301, "AlphaBounce", 8000, 2))
shoppingCart.append(Product(701, "Samsung LED", 40000, 2))

LinkedList.iterateForward(shoppingCart)
print("append----------------------------")
print(" ")
shoppingCart.push(Product(801, "Samsung TV", 40000, 1))
shoppingCart.push(Product(1001, "Sony TV", 30000, 1))
shoppingCart.push(Product(2001, "LG TV", 20000, 1))
print("push++++++++++++")
#
#
#
Stack.iterateBackward(shoppingCart)
print("=====================================================")
shoppingCart=Queue()
shoppingCart.add(Product(901, "Samsung phone", 30000, 1))
shoppingCart.add(Product(9001, "Sony Mobile", 30000, 1))
shoppingCart.add(Product(90001, "LG Mobile", 30000, 1))
Queue.iterateForward(shoppingCart)
# shoppingCart.iterateForward()
print("-------------------------------------")

print("^^^^^poll^^^^^")

Queue.poll(shoppingCart)
Queue.iterateForward(shoppingCart)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

print("pop****************************")
Stack.pop(shoppingCart)
Stack.iterateBackward(shoppingCart)
print("*********************************")



