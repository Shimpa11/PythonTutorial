def hello():
    print("this is Hello Function")
    return "hello"
    # return "Bye" this wont work as this is second return statement and after ist return statement, func frane is destroyed

result=hello()
print("result is: ",result)


# Generator is a function with yield statement
# Executing a function with yield statement(s) makes a function as Generator


def helloAgain():

    print("This is hello again")
    yield "HI"
    yield "Hello"
    yield "bye"
result=helloAgain()
print(result, type(result))# result ia generator object
#  to execute the generator function,  below statement will work
# generator will print data line by line

# next() is built in function where ref of generator object is copied.

print(next(result))
print(next(result))
print(next(result))

# same number of print statements as the number of yield statement
# print(next(result)) # error