

file = open("Session16file(ride).py", "r")

# data = file.read(10)
# print(data)

# print("~~~~~~~~~")

# data = file.read(15)
# print(data)
"""
line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)
line3 = file.readline()
print(line3)
line4 = file.readline()
print(line4)
line5 = file.readline()
print(line5)
"""
lines=file.readlines()
print(type(lines))


print(file.tell())  #0

# Move Cursor Location
file.seek(10)
data = file.read(15)
print(data)

# Tell Cursor Location
print(file.tell())  #25


# functions = 0
# for line in lines:
#     if "def" in line:
#         print(line)
#         functions += 1
classes = 0

for line in lines:
     if "class" in line:
        print(line)
        classes += 1
data=line.split(" ")
print(data)


# print(">> Total classes:", classes)

