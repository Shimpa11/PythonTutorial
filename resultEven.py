number=int(input("Enter number:"))

n1=number//100
print(n1)
n2=number%100
print(n2)
n3=n2//10
print(n3)
n4=n2%10
print(n4)
result=n1+n3+n4
print("Result is:", result)

if result%2==0:
    print("Result is  even")
else:
    print("odd")


