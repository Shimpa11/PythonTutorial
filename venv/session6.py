# main frame and function frame



# num=5
# print("1.num is", num)
#
# print("num is",num)
# def square(n):
#     global num
#     n=n*n
#     num=n
#     print("2. n is:",n)
#     print("3.num is",num)
#       return   Last statement always means return

# square(7)
# print("4.num is", num)


# def square(num): # num, a ref variable that contains hashcode
#     num=num*num
#     print("num is ",num)
#
# num=10# num, a ref variable that contains hashcode
# print("num in main is:",num)
# square(num)
# print("num now is",num)

def square(num): # num is a Reference Variable which holds HashCode of 10
    print(">> [SQUARE] num is:", num, hex(id(num)))
    num = num * num
    print(">> [SQUARE] num now is:", num, hex(id(num)))


num = 10  # num is a Reference Variable which holds HashCode of 10
print(">> [MAIN] num is:", num, hex(id(num)))
square(num)
print(">> [MAIN] num now is:", num, hex(id(num)))