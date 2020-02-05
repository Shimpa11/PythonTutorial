class A:

    # Property of A class
    a = 10

    def __int__(self, b):
        print(">> Object Constructed with init of A")
        self.b = b

    def show(self):
        print(">> a is:", A.a)
        # print(">> b is:", self.b)
class B:

    x = 10

    def __init__(self, y):
        print(">> Object Constructed with init of B")
        self.y = y

    def show(self):
        print(">> x is:", B.x)
        print(">> y is:", self.y)

class C(A, B):
    pass

cRef = C(10)
print(cRef.__dict__)

cRef.show()
print(C.mro())