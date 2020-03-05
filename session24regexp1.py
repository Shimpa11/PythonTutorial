import  re
# number=input("enter the number: ")
email=input("Enter the email: ")



# result=re.search("([A-Z]{2})(\d{2})([A-Z]{2})(\d{4})",number)

# result=re.search("\b[a-zA-Z 0-9_.%]@ [a-zA-Z 0-9_.%]+\.[a-zA-Z 0-9_ .%]",email)
# result=re.search("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",email)


# result=re.search("([A-Za-z0-9_.%]+) @([A-Za-z]+)\.([a-z]{3})",email

result=re.search("([a-zA-Z0-9_ . +-]+ @[a-zA-Z 0-9_]+\.[a-z]{2,8})$",email)
if result:
    print("valid email")
else:
    print("Invalid")



