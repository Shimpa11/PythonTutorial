a=[3,8,9,7,6]
key=a[0]
print(len(a))
for i in range(0,len(a)):
        if i<len(a)-1:
          a[i]=a[i+1]
          # a[i-1]=a[i]

        else:
            a[i]=key

print(a)

# key2=a[0]
# for j in range(0,len(a)):
#     if j<len(a)-1:
#         a[j]=a[j+1]
#     else:
#         a[j]=key2
# print(a)
# # output=[]
# # a=[3,8,9,7,6]
# # for i in range(0,len(a)):
# #     if i<4:
# #         i=i+1
# #     output.append(a[i])
# # print(output)

