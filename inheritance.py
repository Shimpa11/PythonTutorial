# multiple inheritance
class A:
    a=10

    def __init__(self,b):
        print("object constructed init of A")
        self.b=b


    def show(self):
            print("a is ", A.a)
            print("b is ", self.b)
class B:
    x=10
    def __init__(self,y):

        print("object constructed init of B")
        self.y = y

    def show(self):
        print("x is ",B.x)
        print("y is ",self.y)

class C(A,B):
    pass

cref=C(20)
# cref.show()
print(cref.__dict__)
cref.show()