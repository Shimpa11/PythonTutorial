prices={
    "size1":100,
    "size2":150,
    "size3":200
}
print(prices.keys())
print(prices.values())

for key,value in prices.items():
    print (key, "=>",value)
for value in prices.items():
    print(value)