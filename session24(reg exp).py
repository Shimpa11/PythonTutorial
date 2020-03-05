import  re

quote=" The harder you work for something, the greater you will  feel when you achieve it."
result=re.findall(".",quote)
print(result)
print("-------")

result=re.findall("\w",quote)
print(result)
print("-------")


result=re.findall("\w*",quote)
print(result)
print("-------")

result=re.findall("\w+",quote)
print(result),
print("-------")

result=re.match("The",quote)
print(result)
print(type(result))


result=re.search("you",quote)
print(result)
print(type(result))

result=re.findall("you",quote)
print(result)
print(type(result))

data=re.split("the",quote)
print(data)


data=re.split("you",quote)
print(data)

# substitute
data=re.sub("the", "a",quote)
print(data)
