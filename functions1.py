def add(n1,n2):
    n3=n1+n2
    return n3
print(add(2,3))



# default agrs
def add(n1=0,n2=0):
    n3=n1+n2
    return n3
print("the default answer ",add())# even if agrs not given,default values are taken


#positional args
def add(n1=0,n2=0):
    n3=n1+n2
    return n3

#this is an error as agrs are takes left to right so default is n1 and no n2 value

# print(add(3))

print("n1 and n2 changed  ",add(n1=3,n2=5))
print("only one value ,n2 is given",add(n2=9))