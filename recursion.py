
def binary(num):
    if num==0:
        return
    else:

        binary(num//2)
        print(num%2, end=" ")

# base case

number=8
binary(number)


