class CA:
    def __init__(self):
        print("object constructed")


# If you re-define previous function again, it will be deleted

    def __init__(self,num):
        print("second object of CA created and the number is:",num)

# cRef=CA() error
 # In Python, OVERLOADING is not SUPPORTED
 # cref=CA()  error


cRef=CA(10)

# class CA:
#     # In Python, OVERLOADING is not SUPPORTED
#     def __init__(self):
#         print(">> CA Object Constructed")
#
#     # If you re-define previous function again, it will be deleted
#     def __init__(self, num):
#         print(">> CA Object Constructed and num is:",num)
#
#
# cRef = CA(10)
# So, we need to maintain standardization while creating Objects








