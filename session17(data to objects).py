class Customer:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def showCustomerDetails(self):
        print("Name:{}Phone:{} Email:{}".format(self.name,self.phone,self.email))

class Driver(Customer):
    def __init__(self,name, phone,email,licenseNumber):
        Customer.__init__(self,name,phone,email)
        self.licenseNumber=licenseNumber
    def showDriverDetails(self):
        # print("DRIVER DETAILS:{}@@{}@{}@{}".format(self.name, self.phone, self.email,self.licenseNumber))
        print("DRIVER DETAILS")
        self.showCustomerDetails()
        print("License Number",self.licenseNumber)

class Cab:
    def __init__(self,regNumber,basePrice):
        self.regNumber=regNumber
        self.basePrice=basePrice
    def showCabDetails(self):
        print("CAB DETAILS:")
        print("Reg Number: {}, BasePrice: {}".format(self.regNumber,self.basePrice))

class OlaMini(Cab):
    def showCabDetails(self):
        print("Ola Mini DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class OlaMicro(Cab):
    def showCabDetails(self):
        print("Ola Micro DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))

class OlaSedan(Cab):
    def showCabDetails(self):
        print("Ola Sedan DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))

class Ride:

    rideNumber=1

    def __init__(self,customer):
        self.ride=Ride.rideNumber
        self.customer=customer

        Ride.rideNumber+=1


    def SourceAndDestination(self):
        self.source=input("Enter the source: ")
        self.destination=input("Enter the destination: ")
        print("The ride shall be booked from {} to {}".format(self.source,self.destination))

    def SelectCab(self):
        self.cab=None
        print("Select the cab:")
        print("MINI| MICRO | SEDAN")
        choice=input("Enter the type of cab:")
#         runtime polymorphism
        if choice== "MICRO":
            self.cab=OlaMicro("PB10AB1234", 100)
        elif choice == "MINI":
            self.cab = OlaMini("PB10CD4568", 200)
        else:
            self.cab = OlaSedan("PB10EF7890", 300)

    def attachDriver(self,driver):
        self.driver=driver

    def showRideDetails(self):
        print("The ride shall be booked from {} to {}".format(self.source,self.destination))
        print("Ride Number:",self.ride)
        self.cab.showCabDetails()
        self.driver.showDriverDetails()
        self.customer.showCustomerDetails()



# SAVING THE DATA IN FILE(OBJECTS TO DATA {CSV FILES} SERIALIZATION
    def saveRide(self):
        rideData="{},{},{},{},{},{},{},{},{},{},{},{}\n".\
                  format(self.ride,self.source,self.destination,
                   self.cab.regNumber, self.cab.basePrice,
                   self.driver.name, self.driver.phone,
                   self.driver.email, self.driver.licenseNumber,
                   self.customer.name, self.customer.phone, self.customer.email)

        print(rideData)
        file=open("rides1.csv", "a")
        file.write(rideData)
        file.close()

        # print("Ride Saved")
        print(">> Ride[{}] Saved :)".format(self.ride))

    # READING     THE    FILE    CONVERTING    BACK    DATA    FROM    FILE    INTO    OBJECTS

    @staticmethod
    def readRides():
        file = open("rides.csv", "r")
        # line = file.readline()
        lines = file.readlines()

        for line in lines:
            data = line.split(",")
            print(data)
            l = len(data)
            customer = Customer(data[l - 3], data[l - 2], data[l - 1])
            driver = Driver(data[l - 7], data[l - 6], data[l - 5], data[l - 4])
            cab = Cab(data[l - 9], data[l - 8])
            ride = Ride(customer)
            ride.ride = int(data[0])
            ride.source = data[1]
            ride.destination = data[2]
            ride.cab = cab
            ride.attachDriver(driver)
            # customer.showCustomerDetails()
            # driver.showDriverDetails()
            # cab.showCabDetails()



            ride.showRideDetails()

        file.close()

# customer = Customer("John", "98564 56234", "john@example.com")
# driver = Driver("Mike", "99562 56247", "mike@example.com", "AB1015628")

# ride = Ride(customer)
# ride.SourceAndDestination()
# ride.SelectCab()
# ride.attachDriver(driver)
# ride.showRideDetails()
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# Ride.saveRide()
Ride.readRides()

















