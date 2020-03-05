import numpy as np
chessboard=np.zeros((8,8),dtype=int)
print(chessboard)
print("=================")

# slicing /filteration and Substitution

 # Start from 1 and go till end | Row Filter
# Filter :)
# print(chessboard[1::2])
# 0::2 \ column filter
chessboard[1::2, 0::2]=1
chessboard[0::2, 1::2]=1

print(chessboard)

def rowCheck():
    pass
def columnCheck():
    pass
def diagonalCheck():
    pass

indexes=[]
for i in range(0,len(chessboard)):
    print("Where would you like to place the Queen #{}".format(i+1))
    i=int(input("Enter row Position: "))
    j=int(input("Enter column position: "))

    # boundary conditions
    if(i>=0 and i<=7) and (j>=0 and j<=7):
        chessboard[i][j]=9
    else:
        print("Please enter correct position")
    indexes.append([i,j])
print("====Final Chessboard====")
print(chessboard)
print("====Final Queens====")
print(indexes)
