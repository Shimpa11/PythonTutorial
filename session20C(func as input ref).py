#function with input as a reference
def hello(fun):
    print("hello...")
    fun()
def bye():
    print("bye...")
def show(num=10): #default argument
    print("showing",num)


#passing function as ref or argument
hello(fun=bye)
print("####################")
# to pass function as ref or argument , passed function should have default arguments
hello(fun=show)

# Factory Design Pattern
# Create with help of Concept called Polymorphism (Run Time)
def loginWithFacebook():
    print("Login with Facebook")
def loginWithGoogle():
    print("Login with Google")

def loginWithGithub():
    print("Login with Github")
def login(type):
    type()
print("---------------")
print("1.Login with Facebook")

print("---------------")
print("2.Login with Google")

print("---------------")
print("3.Login with Github")

choice=int(input("Select your login type:"))
if choice==1:
    login(loginWithFacebook)
elif choice==2:
    login(loginWithGoogle)
elif choice==3:
    login(loginWithGithub)
else:
    print("Enter valid choice")