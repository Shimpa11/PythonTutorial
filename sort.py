
products = [1541, 2451, 1353, 4673, 5245, 2356, 6777, 8234, 9231, 1331]
# for i in range(0, len(products)):
#
# #     print(products[i])
#
#       if products[i]>5000:
#           products[i]=products[i]-0.4*products[i]
#          % print(products[i])
# for i in range(0,len(products)):
#     print("new price after discount",products[i])




# a=[12,11,5,9,1]
# #for i in range(0,len(a)):
#    # print(a[i])
# for i in range (1,len(a)):
#     key=a[i]
#     hole=i
#     while  hole>0 and key<a[hole-1]:
#         a[hole]=a[hole-1]
#         hole=hole-1
#         a[hole]=key
# for i in range(0,len(a)):
#     print(a[i])

for i in range(1, len(products)):
    key=products[i]
    hole=i
    while hole>0 and products[hole-1]>key:
        products[hole]=products[hole-1]
        hole=hole-1
        products[hole]=key
for i in range(0,len(products)):
    print(products[i])


