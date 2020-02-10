"""
  DataBase
	Permanent Data Store :)
	Prefer DataBase over Files :)
	> 1. Security
	> 2. Centralization
	> 3. Operations | Time Optimized
		 Insert
		 Update
		 Delete
		 Fetch/Query/Retrieve
	> 4. Structured Data Storage
	     We have Tables
	     In Tables we have rows
	     and in rows we have data as columns :)
	> 5. DataBase Represents a Data Structure
	examples:
	MySQL and Oracle 	| SQL
	Tree Data Structure
	FirebaseFirestore	| No SQL
	Tree Data Structure
	Neo4J				| No SQL
	Graph Data Structure
	ORM (Object Relational Mapping)
	SQL
	1. Create Table
    create table Customer(
        id int primary key auto_increment,
        name varchar(256),
        phone varchar(20),
        email varchar(256)
    )
    2. Insert Data Into Table
    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')
    STEPS to Perform DB Interaction
    1. Download the library and install it in your Python Project
       > Settings of your project
       > execute pip install command on terminal
    2. Write SQL Statement to be executed and substitute the data
    3. import mysql.connector in your program
    4. Create Connection to DataBase with library
    5. Obtain Cursor from Connection to execute SQL Statement
    6. Execute SQL Statement and Commit It :)
"""
# data manipulation in table also known as write operation
# insert operation
 # updata operation    update Customer set name="john watson', phone='98544 85624'  where id=1
# delete operation   delete from Customer where id=1


#  [read operations]  Fetch/Query
# select * from  Customer

import mysql.connector as lib
class Customer:

    def __init__(self,mode):
        if mode==1:
            self.id=0
            self.name=input("Enter Customer name:")
            self.phone = input("Enter Customer phone:")
            self.email = input("Enter Customer email:")
        elif mode==2:
            self.id = int(input("Enter Customer ID: "))
            self.name = input("Enter Customer name:")
            self.phone = input("Enter Customer phone:")
            self.email = input("Enter Customer email:")
        else:
            pass
    def showCustomerDetails(self):
        print("@@{}@{}@{}".format(self.name,self.phone,self.email))

def executeSQL(sql):
        conn = lib.connect(user="root", password="", database="Customer", host="127.0.0.1", port="3306")
        print("Connection created")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

repeat="yes"
while repeat == "yes":
    print("===Customer Management App===")

    print("1.Register the customer")
    print("2.Update  the existing customer")
    print("3.Delete the  existing customer")

    print("4.View all  customers")
    print("5.View Customers by ID")
    print("6.View Customers by phone")

    choice=int(input("Enter your choice:"))
    if choice==1:
            customer=Customer(1)
            customer.showCustomerDetails()

            save=input("Would you like to save customer Yes/No: ")
            if save=="yes":
                sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
                executeSQL(sql)
            print("CUSTOMER SAVED :)")

    elif choice == 2:
        customer=Customer(2)
        customer.showCustomerDetails()
        save = input("Would you like to update customer Yes/No: ")
        if save == "yes":
            sql= "update Customer set name= '{}', phone='{}', email='{}' where id={}".format(customer.name,customer.phone,customer.email,customer.id)
            executeSQL(sql)
            print("CUSTOMER UPDATED")
    elif choice==3:
        id=int(input("Enter customer id to be deleted: " ))
        delete = input("Would you like to Delete Customer? (yes/no): ")
        if delete=="yes":
            sql="delete from Customer where id={}".format(id)
            executeSQL(sql)
            print("CUSTOMER Deleted")
    elif choice==4:
    # sql = "select id, name from Customer"

        sql="select * from Customer"
        conn = lib.connect(user="root", password="", database="Customer", host="127.0.0.1", port="3306")
        cursor = conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        # print(rows)
        # print(type(rows))
        for row in rows:
            customer=Customer(3)
            customer.id=row[0]
            customer.name=row[1]
            customer.phone = row[2]
            customer.email = row[3]
            # print(row)
            customer.showCustomerDetails()
        print("CUSTOMER shown")
    elif choice==5:
        id = int(input("Enter Customer ID to be Searched: "))
        sql="select * from Customer where id={}".format(id)
        conn = lib.connect(user="root", password="", database="Customer", host="127.0.0.1", port="3306")
        cursor = conn.cursor()
        cursor.execute(sql)
        row=cursor.fetchone()
        if row is not None:
            print(row)
        else:
            print("Record not found")
    elif choice==6:
        phone=input("Enter the phone to be searched: ")
        sql="select * from Customer where phone='{}'".format(phone)
        conn=lib.connect(user="root", password="",database="Customer",host="127.0.0.1",port="3306")
        cursor=conn.cursor()
        cursor.execute(sql)
        row=cursor.fetchone()
        if row is not None:
            print(row)
        else:
            print("Customer with {} phone number not found".format(phone))
    else:
        print("Enter a valid choice: ")
    repeat = input("Would You Like to Re Use App (yes/no): ")








