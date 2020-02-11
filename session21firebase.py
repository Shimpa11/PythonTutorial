
"""
Install Firebase admin library
pip install firebase-admin
for upgrade pip
python -mpip install -U --force-reinstall pip

go to firebase.google .com
create  a new project

3. create Database inyour account

clloud firestore

test mode

"""

#
# import firebase_admin
# print("This is Awesome")




import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
print("Firebase configured and initialized")



# MODEL
class Customer:
    def __init__(self):
            self.name=input("Enter the customer name: ")
            self.phone = input("Enter the customer phone: ")
            self.email = input("Enter the customer email: ")



    def showCustomerDetails(self):
        print("{} | {} | {} ".format(self.name, self.phone, self.email))

#APPLICATION
def main():
    customer=Customer()
    customer.showCustomerDetails()
    customerData=customer.__dict__
    print(customerData,type(customerData))

# db is reference to firestore database


    db=firestore.client()
    db.collection("customers").document(customer.email).set(customerData)
    print('CUSTOMER SAVED')


if __name__ == "__main__":
    main()

