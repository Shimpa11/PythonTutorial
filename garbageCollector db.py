import mysql.connector as lib

class DB:
    def __init__(self):
        self.conn=lib.connect(user="root",password="",database="GarbageCollector", host="127.0.0.1",port="3306")


    def executeReadOperations(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        return rows

db=DB()
class Customer:

    def __init__(self,mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter Customer name:")
            self.phone = input("Enter Customer phone:")
            self.property=input("Enter Customer property:")

        elif mode == 2:
            self.id = int(input("Enter Customer ID: "))
            self.month = input("Enter Month name:")
            self.year = input("Enter year:")
        else:
            pass
    def showCustomer(self):
        print("{}|{}".format(self.name,self.phone))
        print("{}".format(self.property))

    def showBills(self):

        print("{}".format(self.id))
        print("{}|{}".format(self.month,self.year))

class Property:
    # prices = {"100sq": 100, "200sq": 150, "300sq": 200, }
    # prices = {"size1": 100, "size2": 150, "size3": 200, }

    def __init__(self,size,fee):
        self.size=size
        self.fee=fee
    def showProperty(self):
        print("{}| {}".format(self.size,self.fee))

class Bill():
    # def __init__(self):

    def calculateBill(self):
        prices = {"size1": 100, "size2": 150, "size3": 200, }

        totalBill = 0
        for k,v in prices.items():
            print(k,v)
            if k in prices:
            # if customer.property==prices.:

                   totalBill=totalBill+prices[k]
        print(totalBill)
b1=Bill()
b1.calculateBill()


def executeSQL(sql):
        conn = lib.connect(user="root", password="", database="GarbageCollector", host="127.0.0.1", port="3306")
        print("Connection created")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

print("===Garbage Collector App===")

print("1.Add the customer")
print("2.Show the  customer bill")
print("3.Show saved  customer ")

repeat="yes"
while repeat=="yes":
    choice=int(input("Enter your choice:"))
    if choice==1:
        customer=Customer(1)
        customer.showCustomer()

        save=input("Would you like to save customer Yes/No: ")
        if save=="yes":
            sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.property)
            executeSQL(sql)
            print("CUSTOMER SAVED :)")

    if choice == 2:
        customer = Customer(2)
        # customer.showBills()

        save = input("Would you like to save bill Yes/No: ")
        if save == "yes":
            sql = "insert into bills values('{}', '{}',{})".format(customer.month,customer.year,customer.id)
            executeSQL(sql)
            print("BILL SAVED")
    elif choice == 3:
        id = int(input("Enter the customer id to be searched:"))
        sql = "select * from Customer where id={}".format(id)
        rows = db.executeReadOperations(sql)
        for row in rows:
            customer=Customer(3)
            customer.id=row[0]
            customer.name = row[1]
            customer.phone = row[2]
            customer.property = row[3]
            customer.showCustomer()


        # if rows is not None:
        #     print(rows)
        # else:
        #     print("Customer with {} id  not found".format(id))
    else:
        print("Enter the valid choice:")


