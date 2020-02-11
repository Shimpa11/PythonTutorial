def dataGenerator():
    file=open("point.csv","r")
    lines=file.readlines()
    for line in lines:
        yield line
result=dataGenerator()
# the result will refer to generator object

print(result)
print(type(result))

# to execute the generator functiom

print(next(result))
print(next(result))
