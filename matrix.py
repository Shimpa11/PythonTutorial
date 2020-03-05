A=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a=A[0]
temp=a
b=A[1]
c=A[2]
# print(a,b,c)
# print(len(A))
for i in range(len(A)):
     for j in range(len(A)):
         # print(A[i][j])
         A[j][i]= A[i][j]
a=A[0]
print(a)
b=A[1]
print(b)


     # print(A[i][j], end=" ")
# print()

