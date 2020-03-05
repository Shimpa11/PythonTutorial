pixel1 = [100, 85, 125]
pixel2 = [120, 15, 12]
pixel3 = [12, 105, 212]
pixel4 = [150, 85, 158]
pixel5 = [200, 155, 102]
pixel6 = [120, 105, 12]
pixel7 = [10, 80, 105]
pixel8 = [12, 105, 120]
pixel9= [122, 255, 200]

Image =   [ [pixel1, pixel2, pixel3],
           [pixel4, pixel5 ,pixel6],
           [pixel7, pixel8, pixel9]

          ]
for i in range(len(Image)):
    for j in range(len(Image)):
        print(Image[i][j],"\n",end="")

        Image[i][j]=Image[j][i]

        print(Image[i][j],end="" )
# print(len(Image))