class garbageCollector:

    def __init__(self,name,customer):
        self.name=name
        self.customer=customer
    def showCollector(self):
        print("{}".format(self.name))
        self.customer.showCustomer()
        print("---------------")

    @staticmethod
    def readBill():
        file=open("customer.csv","r")
        lines=file.readlines()
        for line in lines:
            data=line.split(" ")
            bill=garbageCollector(data[2])
            bill.customer=data[0]
            bill.saveBill()
        file.close()


    def saveBill(self):
        file = open("collection.csv", "a")
        billData = self.showBill()
        file.write(billData)
        file.close()
        print("Bill SAVED")


class customer:
    # customerid = 1
    def __init__(self,name,phone,address,month,year,property):
        # self.cid = customer.customerid
        self.name=name
        self.phone=phone
        self.address=address
        self.month=month
        self.year=year
        self.property = property
    def showCustomer(self):
        print("{}|{}".format(self.name,self.phone))
        print("{}|{}|{}|{}".format(self.address, self.month,self.year,self.property))
        self.property.showProperty()
    def saveCustomer(self):
        return "{}|{}|{} \n".format(self.name, self.phone, self.property)

    def save(self):
        file = open("customer.csv", "a")
        customerData = self.saveData()
        file.write(customerData)
        file.close()
        print("DETAILS SAVED")



class property:
    def __init__(self,size,fee):
        self.size=size
        self.fee=fee
    def showProperty(self):
        print("{}| {}".format(self.size,self.fee))


# c2=customer("Fionaa","99999 88888","Redwood ","200sq",1,2020)

p1=property("100sq", 100)
p2=property("200sq", 150)
p3=property("300sq", 200)
p4=property("400sq", 250)
p5=property("500sq", 300)




properties=[p1,p2,p3,p4,p5]
c1=customer("John","90909 80808","Redwood Shores","1","2020",p1)
c2=customer("Fionaa","99999 88888","Redwood ",1,2020,p2)
c3=customer("Sam","90009 80008","Shores ",1,2020,p3)




gc=garbageCollector("GC",c1)
gc.showCollector()

c1.showCustomer()
c1.saveCustomer()
c2.saveCustomer()
c3.saveCustomer()




