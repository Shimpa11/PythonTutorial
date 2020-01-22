# passing the reference(hashcodes)

def square(numbers):
    print("[square] numbers",numbers,hex(id(numbers)))

    for i in range(0,len(numbers)):
        numbers[i]=numbers[i]*numbers[i]
    print(" [square]numbers  now is", numbers, hex(id(numbers)))

numbers=[10,20,30,40,50]
print("number[0] is",numbers[0],hex(id(numbers[0])))

print( "[main] numbers is" ,numbers,type(numbers),hex(id(numbers)))


# numbers[1]=222
# print(numbers,type(numbers))

square(numbers)
print("[main] numbers now is",numbers, hex(id(numbers)))
print("number[0] is",numbers[0],hex(id(numbers[0])))


