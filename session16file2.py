file=open("session 7.py","r")
# read all operation
data=file.read()
print(data)
print("~~~~~~~~~~~~~")

# Re-Read the file which is already Read
# We will not get the contents once, file is read completely
# data = file.read() # We will not get any data :(
# print(data)