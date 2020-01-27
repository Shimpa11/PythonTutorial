name="Fionaa"
age=20
print("the name is {}. Her age is {}.".format(name,age))
print("Welcome to the app %s" %(name))
print("Welcome to the app", name)

products = [3454, 2411, 1341, 4568, 8976]
for i in range(0,len(products)):
    oldPrice=products[i]
    products[i]=products[i]-0.4*products[i]
    newPrice=products[i]
    print("{} is changed to {}".format(oldPrice,newPrice))
#
# cid=int(input("enter cid:"))
# cname=input("Enter cname:")
#
# sql="insert into customer values('{}' ,'{}')".format(cid, cname)
# print("SQL is",sql)


print("^^^^^^^^^^dictionary^^^^^^^^^")
employee={
    "name":"Fionna",
    "age":20,
    "eid":10
}
print("the employee",employee,type(employee))
print(len(employee))
print(max(employee))
print(min(employee))

# update and delete dict

employee["name"]="nancy"
print(employee)



employee["address"]="park avenue"
print(employee)

del employee["eid"]
print(employee)

# del employee
# print(employee)  err

keys=list(employee.keys())
value=list(employee.values())

print("the key is :",keys, type(keys))
print("the values is:" , value,type(value))

name="shimpa"
name1="Shimpa"
print(max(name))
print(min(name))
print(max(name,name1))