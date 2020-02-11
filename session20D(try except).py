# Errors Generated at Run Time are called Run Time Error : Exceptions
# Exceptions are no good for our programs :(
# It will hamper performance of OS

print("---------------")
print("APP STARTED")
print("---------------")

numbers=[10,20,30,40,50,60,70,80,90]
idx=int(input("Enter your lucky number:"))

try:
    print("you won a prize of", numbers[idx])
    print("This is awesome")
    print("please enter you bank details to send money")
except Exception as e:#  for all type of error
    print("some error:",e)

    #a block that executes before the process dies
finally:
    print("Thank you for playing game")



"""
except IndexError as idxErr:
        print("some error as",idxErr)
except ZeroDivisionError as zdErr:
        print("some error as",zdErr)
"""


print("----------------")
print(">> APP Finished :)")
print("----------------")

# Whenever error at run time will occur, it will crash the program
# Program Terminates Abnormally