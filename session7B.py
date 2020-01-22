data=[1,2,3,4,5]
print(len(data))
print((max(data)))


# list comprehension , dont work on expressions

print([x**2 for x in data])
productPrices=[1235,5625,7845]
print([0.4*x for x in productPrices])
# list comprehension , dont work on expressions
# print(x[x-0.4*x for x in productPrices])