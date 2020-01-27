# s1={1,2,3,4,5,2}
# s2={3,4,5,6}
#
# s3=s1 | s2    #union
# print(s3)
# s3 =s2&s3   #intersection        (mutual)
# print(s3)
# s3=s1-s2    #difference
# print(s3)

# hetrogeneous sets
s1={1,2,3,'A','B','C'}
s2={1,2,3,'A'}
s3=s1.intersection(s2)
s4=s1.union(s2)
s5=s1.difference(s2)

# real time use case
s6=s1.symmetric_difference(s2)
print(s6)
s1.add('x')
print(s1)
s1.remove(1)
print(s1)
s1.pop()  #  clears first element of teh set
print(s1)

# manipulation of data structure
s={10,20,30}
l=list(s)
print(l)
l=[10,20,30,20]
s==set(l)
print(s)
print(s2.issubset(s1))
print(s1.issuperset(s2))



quotes="live life king size"
for i in range(0, len(quotes)):
    print(quotes[i], end= "* ")
print("**********strings*********")
songName="hello.mp3"
if songName.endswith(".mp3"):
    print("valid format")
else:
    print("invalid format")
number="100"
print(number.isdigit())
print(type(number))

data="be happy"
data2=data.split(" ")
print(data2)

print(data3=data.strip('happy'))

print(data3=data.strip())