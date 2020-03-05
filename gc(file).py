import os
feeStructure={
    "100":100, "200":150, "300":200, "400":250,"500":300
}
class Property:
    def __init__(self,houseNum=None,block=None,street=None,area=None,size=None):
        self.houseNum=houseNum
        self.block=block
        self.street=street
        self.area=area
        self.size=size
    def inputPropertyDetails(self):
        self.houseNum = input("Enter House Num:")
        self.block = input("Enter House block:")
        self.street = input("Enter House street:")
        self.area = input("Enter House area:")
        self.size = int(input("Enter House size:"))

    def showProperty(self):
        print("{}|{}|{}|{}|{}".format(self.houseNum,self.block,self.street,self.area,self.size))

    def toCSV(self):
        return "{},{},{},{},{}".format(self.houseNum,self.block,self.street,self.area,self.size)

class Customer:
    def __init__(self,name=None,phone=None,email=None,property=None):
        self.name=name
        self.phone=phone
        self.email=email
        self.property=property

    def inputCustomerDetails(self):
        self.name = input("Enter Customer name:")
        self.phone = input("Enter Customer phone:")
        self.email = input("Enter Customer email :")

        # Has-A Relationship
    def linkPropertyToCustomer(self, property):
        self.property=property


    def showCustomer(self):
        print("{}|{}|{}".format(self.name,self.phone,self.email))
        self.property.showProperty()

    def toCSV(self):
        return "{},{},{},{} \n".format(self.name,self.phone,self.email,self.property.toCSV())

class Fee:
    def __init__(self,phone=None,month=None,year=None,amount=None):
        self.phone=phone
        self.month=month
        self.year=year
        self.amount=amount

    def inputFeeDetails(self):
        self.phone = input("Enter Customer Phone: ")
        self.month = int(input("Enter month: "))
        self.year = int(input("Enter year: "))

    #     amount to be fetched automatically
        file = open("gc-customers.csv" ,"r")
        lines=file.readlines()

        # implementing linear search on list
        for line in lines:
            data = line.split(",")
            # print(data)
            if data[1] == self.phone:
                size = data[len(data) - 1].strip()
                self.amount = feeStructure[size]
                break
        if os.path.isfile("gc-fees.csv"):

                lastMonth=self.getLastFeePaidMonth()

                difference=self.month-lastMonth
                if difference==1:
                    print("Fee to be paid on {} month {} year: \u20b9 {}".format(self.month,self.year,self.amount))
                    self.savefees()
                else:
                    fixedAmount = self.amount
                    newAmount=(difference-1)*(self.amount+0.1*self.amount)
                    self.amount=newAmount+fixedAmount

                    print("Fee not paid for {} months.Please pay{}".format(difference,self.amount))
                    self.savefees()
        else:
            self.savefees()

    # fetching last month fee
    def getLastFeePaidMonth(self):
    #
        file=open("gc-fees.csv","r")
        lines=file.readlines()
        lastfeeLine = None
        for line in lines:
            # getting lines and splitting
            data=line.split(",")
            print(data)
            if data[0]==self.phone:
                lastfeeLine=line
        data=lastfeeLine.split(",")
        month=int(data[1])
        return month



    def showFee(self):
        print("{}|{}|{}|{}".format(self.phone,self.month,self.year,self.amount))

    def toCSV(self):
        return  "{},{},{},{}".format(self.phone,self.month,self.year,self.amount)
    def savefees(self):
        data = self.toCSV()
        print(data)
        save = input("Would you like to save fee{} for {} month (yes/no): ".format(self.amount, self.month))
        if save == "yes":
            file = open("gc-fees.csv", "a")
            file.write(data)
            file.close()
            print(">> Fee detail saved in file")

def main():

    print("======Garrbage Collector App========")
    print("1.Add Customer")
    print("2.Charge Garbage Fee")

    choice=int(input("Enter your choice: "))
    if choice==1:
        property=Property()
        property.inputPropertyDetails()

        customer=Customer()
        customer.inputCustomerDetails()

        customer.linkPropertyToCustomer(property)

        customer.showCustomer()
        data=customer.toCSV()
        print(data)

        save=input("Would you like to save customer {} (Yes/no): ".format(customer.name))
        if save=="yes":
            file=open("gc-customers.csv","a")
            file.write(data)
            file.close()
            print(">>Customer data saved in file")

    elif choice==2:
        fee = Fee()
        fee.inputFeeDetails()
        fee.showFee()

    # data=fee.toCSV()
    # print(data)
    # save=input("Would you like to save fee{} for {} month (yes/no): ".format(fee.amount,fee.month))
    # if save== "yes":
    #     file=open("gc-fee.csv","a")
    #     file.write(data)
    #     file.close()
    #     print(">> Fee detail saved in file")y

    else:
        print("Enter a valid choice")

if __name__ == "__main__":
    main()
