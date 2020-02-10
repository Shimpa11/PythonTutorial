def fun():
    print("This is fun Session19")

class CA:
     def __init__(self):

         print("CA object constructed")
fun()
cRef=CA()

def main():
    a = 10
    b = a ** 2
    print(">> This is suppose to be executed :)", b)

if __name__ == "__main__":
    main()
