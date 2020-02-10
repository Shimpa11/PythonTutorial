

"""
PS: https://www.w3schools.com/sql/sql_foreignkey.asp
    JOINS :)
create table Customer(
	id int primary key auto_increment,
	name varchar(256),
	phone varchar(256),
	email varchar(256)
)
create table Orders(
	oid int primary key auto_increment,
	price int,
	id int,
	foreign key (id) references Customer(id)
)


# CONTROLLER
# DAO | Data Access Object | Design Pattern singleton design pattern, single connection throughout. db=DB()
"""
import mysql.connector as lib
class DB:
    def __init__(self):
        self.conn=lib.connect(user="root",password="",database="Customer", host="127.0.0.1",port="3306")

    def executeWriteOperations(self,sql):
        cursor=self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def executeReadOperations(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        return rows

db=DB()

# MODEL
class Customer:
    def __init__(self,mode):
        if mode==1:
            self.id=0
            self.name=input("Enter the customer name: ")
            self.phone = input("Enter the customer phone: ")
            self.email = input("Enter the customer email: ")
        elif mode==2:
            self.id=int(input("Enter the customer ID: "))
            sql="select * from Customer where id={}".format(id)
            rows=db.executeReadOperations(sql)
            print(rows[0])

        else:
            pass
    def showCustomerDetails(self):
        print("{} | {} | {} | {}".format(self.id, self.name, self.phone, self.email))

#APPLICATION
def main():
 # VIEW
    repeat="yes"
    while repeat=="yes":
        print("1.Register the new customer")
        print("2.Update the existing customer")
        print("3.Delete the existing customer")
        print("4.View all customers")
        print("5.View the customer by ID")
        print("6.View the customer by phone")


        choice=int(input("Enter your choice: "))
        if choice==1:
            customer=Customer(1)
            customer.showCustomerDetails()

            save=print("Would you like to save the customer? (Yes/No): ")
            if save=="yes":
                sql="insert into Customer values(null,'{}','{}', '{}')".format(customer.name,customer.phone,customer.email)
                db.executeWriteOperations(sql)
                print('CUSTOMER SAVED')

        elif choice==2:
            customer=Customer(2)
            customer.showCustomerDetails()

            save=print("Would you like to update the customer? (Yes/No): ")
            if save=="yes":
                sql="update customer set name='{}',phone='{}',email='{}'".format(customer.name,customer.phone,customer.email)
                db.executeWriteOperations(sql)
                print("CUSTOMER UPDATED")
        elif choice==3:
            id=int(input("Enter the customer ID to be deleted: "))
            sql="delete from Customer where id= {}".format(id)
            db.executeWriteOperations(sql)
            print(" CUSTOMER DELETED")

        elif choice==4:
            sql="select * from Customer "
            rows=db.executeReadOperations(sql)
            for row in rows:
                customer=Customer(3)
                customer.id=row[0]
                customer.name=row[1]
                customer.phone=row[2]
                customer.email=row[3]
                print(row)
                customer.showCustomerDetails()
            print("customer shown")

        elif choice==5:
            id=int(input("Enter the customer ID to be searched: "))
            sql="select * from customer where id={}".format(id)
            rows=db.executeReadOperations(sql)
            if rows is not None:
                print(rows)
            else:
                print("Record not found")

        elif choice==6:
            phone=int(input("Enter the customer phone to be searched:"))
            sql="select * from Customer where phone='{}'".format(phone)
            rows=db.executeReadOperations(sql)
            if rows is not None:
                print(rows)
            else:
                print("Customer with {} phone  not found".format(phone))
        else:
            print("Enter the valid choice:")



        repeat=input("Would you like to re-use the app? (yes/no):")

if __name__ == "__main__":
    main()












