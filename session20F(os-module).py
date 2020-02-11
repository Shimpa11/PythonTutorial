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

files1 = os.walk("/Users/win/Downloads")
print(files1)
allFiles = list(files1)
for root,dirs,files in files1:
    for file in files:
         if file.endswith('.jpg'):
            print(os.path.join(root,file))
