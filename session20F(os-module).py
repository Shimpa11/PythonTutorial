import os
cwd=os.getcwd()
print(cwd)
print(os.name)
# print(os.uname())
print(os.getlogin())
print(os.getppid())
pathToDirectory="/Users/win/PycharmProjects/PythonTutorial"
pathToFile="/Users/win/PycharmProjects/PythonTutorial/session19A.py"

print("Is PythonTutorials Existing:",os.path.isdir(pathToDirectory))
print("Is session19A.py existing:",os.path.isfile(pathToFile))

pathD="/Users/win/PycharmProjects/PythonTutorial/newProjects"
print("Is newprojects existing:",os.path.isdir(pathD))
if os.path.isdir(pathD)==False:
    os.mkdir(pathD)
    print("Directory created")
    # os.rmdir(path)
# files=os.walk("/Users/win/PycharmProjects/PythonTutorial")
# print(files)
# print(type(files))
#
# allFiles=list(files)
# for file in allFiles:
#     print(file)

files = os.listdir("D:/Angeline")
print(files)
allFiles = list(files)
image = []
iCount = 0

dCount=0
document=[]


fExtn=input("Enter file extension: ")
for file in allFiles:
    if fExtn=="jpg":
        image.append(file.join("D:/Angeline", + '.',+ fExtn))
        iCount+=1
# print(image)
        print(iCount)

    elif fExtn =="pdf":
        document.append(file)
        dCount+=1
        # print(document)
        print(dCount)

    # elif file.endswith('.mp3'):
    #     pass

    else:
        pass





            #
            # elif file.endswith('.mp4'):
            #     print(file)




