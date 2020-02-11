def hello():
    print("hello...")
    # Nested function or inner function
    # helper functio
    def bye():
# nested func will execute only inside the function
# not outside the main function
        print("bye...")

    print(bye)
    bye()
print(hello)
# this wont work
# print (bye)
# bye() wont work as outside the outer function
hello()