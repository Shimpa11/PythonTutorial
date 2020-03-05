import os

file=os.listdir("D:/Angeline")
allfiles=list(file)

print(allfiles, "\n")
print(len(allfiles))

f="docx"
image=[]
iCount=0


for file in allfiles:
    print(file)
    # if f=="jpg":
    #     image.append(file)
    #     iCount+=1
    #     print(iCount)
    # print(image)