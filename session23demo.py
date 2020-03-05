# import  tkinter
from tkinter import *
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
print(">> Firebase Configured and Initialized :)")

class Customer:
    def __init__(self,name=None,phone=None,email=None):
        self.name=name
        self.phone=phone
        self.email=email
    def showCustomer(self):
        print("{}| {}| {}".format(self.name,self.phone,self.email))


def clickHandler():
    print("button clicked")
    customer=Customer()

    customer.name=entryName.get()
    customer.phone=entryPhone.get()
    customer.email=entryEmail.get()

    customer.showCustomer()
    customerData=customer.__dict__
    print(customerData)

    db=firestore.client()
    db.collection("MyCustomers").document(customer.email).set(customerData)
def callbackFunc(event):
    print("combo box option selected")

# Creating a Window :)
# Window is a frame with minimize, maximize and close buttons
window=Tk()
window.title("GUI")
window.geometry("300x300")

lblTitle=Label(window,text="Customer Management Solution")
lblTitle.pack()

lblName=Label(window,text="Enter Customer Name")
lblName.pack()

entryName=Entry(window)
entryName.pack()


lblPhone=Label(window,text="Enter Customer Phone")
lblPhone.pack()

entryPhone=Entry(window)
entryPhone.pack()

lblEmail=Label(window,text="Enter Customer Email")
lblEmail.pack()

entryEmail=Entry(window)
entryEmail.pack()

btnAddCustomer=Button(window,text="Add Customer", bg="yellow", fg="red",command=clickHandler)
btnAddCustomer.pack()

combo=ttk.Combobox(window,values=["Sunday","Monday","Tuesday","Wednesday","Thursday"])
combo.current(2)
# combo.grid(column=0,row=0)
combo.bind("<<ComboboxSelected>>" ,callbackFunc)
# Show the window in an infinite loop :)
window.mainloop()
