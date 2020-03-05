import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
print("Firebase configured and initialized")
db = firestore.client()

class Customer:
    def __init__(self,mode=0):
        if mode==1:
            self.name=input("Enter the customer name: ")
            self.phone = input("Enter the customer phone: ")
            self.email = input("Enter the customer email: ")
        elif mode==2:
            self.email=input("Enter customer id to be updated: ")
            self.name = input("Enter the customer name: ")
            self.phone = input("Enter the customer phone: ")
            self.email = input("Enter the customer email: ")
        else:
            pass


    def showCustomerDetails(self):
        print("{} | {} | {} ".format(self.name, self.phone, self.email))



#APPLICATION
def main():
    repeat="yes"
    # db is reference to firestore database

    while  repeat == "yes":

        print("==Welcome to Customer Management App==")
        print("1. Register New Customer")
        print("2. Update Existing Customer")
        print("3. Delete Existing Customer")
        print("4. View All Customers")
        print("5. View Customer by ID")
        print("6. View Customer by Phone")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer=Customer(1)
            customer.showCustomerDetails()
            customerData=customer.__dict__
            print(customerData,type(customerData))
    #  set-> insert and update
            db.collection("NewCustomers").document(customer.email).set(customerData)
            print('CUSTOMER SAVED')

        elif choice==2:
            customer=Customer(2)
            customer.showCustomerDetails()
            customerData=customer.__dict__
            save = input("Would you like to Update Customer? (yes/no): ")
            if save == "yes":
                db.collection("NewCustomers").document(customer.email).set(customerData)
                print("CUSTOMER UPDATED")

        elif choice==3:
            id=input("Enter customer id to be deleted: ")

            save=input("Would you like to delete Customer? (yes/no): ")
            if save == "yes":
                db.collection("NewCustomers").document(id).delete()
                print("CUSTOMER DELETED")
        elif choice==4:
            id = input("Enter customer collection to be displayed: ")
            docs = db.collection("NewCustomers").stream()
            for doc in docs:
                if doc.exists:
                    print("{} => {}".format(doc.id,doc.to_dict()))
                else:
                    print("Collection not found")


        elif choice==5:
            id = input("Enter customer id to be displayed: ")
            docRef = db.collection("NewCustomers").document(id).get()
            docDict = docRef.to_dict()
            print(docDict)

        elif choice==6:
            phone = input("Enter customer phone to be displayed: ")
            docRef = db.collection("NewCustomers").document(phone).get()
            docDict = docRef.to_dict()
            print(docDict)

        else:
            print("Enter a valid choice")

        repeat=input("Would you like to resuse the App (Yes/No): ")


if __name__ == "__main__":
    main()