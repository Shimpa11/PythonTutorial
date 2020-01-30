class Client:
    def __init__(self, name, phone, email, gender, address, clientType,age,
                 weight,height,package):

        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address
        self.clientType=clientType
        self.age=age
        self.weight=weight
        self.height=height
        self.package=package
    def showClient(self):
        print("{}".format(self.name))
        print( "{} \t {}\t{}\t{}\t{}%%%{}%{}%{}".format(self.phone, self.email, self.gender,
                                          self.address, self.clientType,self.age,
                                             self.weight,self.height))





class Packages:
    def __init__(self, name, price,rating,duration,plan):
        self.name = name
        self.price=price
        self.rating=rating
        self.duration=duration
        self.plan=plan

    def displayPackage(self):
        print("^^^^{}^^^^".format(self.name))
        print("{}.....{}.....{}".format(self.price,self.rating,self.duration))
        print("*********************************")

        for plan in self.plan:
            plan.displayWorkout()
        print("=================================")
        print("%%%%")


class workOutPlan:
    def __init__(self,type,location):
        self.type=type
        self.location=location
        # self.timeslot=timeslot

    def displayWorkout(self):
        print("^^^^{}^^^^{}^^^^".format(self.type,self.location))



# plan1=workOutPlan("yoga","clientHome","Morning")
# plan2=workOutPlan("cardio","clienthome","Morning")
# plan3=workOutplan("weightloss","clienthome","Morning")
# plan4=workOutplan("Aerobics","clienthome","Morning")



# plan=[plan1,plan2,plan3,plan4]




# workOutPlan("yoga","clientHome""Morning"),
#                                 workOutPlan("cardio","clienthome","Morning"),
#                                 workOutPlan("weightloss","clienthome","Morning"),
#                                 workOutPlan("Aerobics","clienthome","Morning")]
package1=Packages("Diomond",2500,5,"3 months",[
                                workOutPlan("yoga","clientHome"),
                                workOutPlan("cardio","Trainer's place"),
                                workOutPlan("weightloss","clientHome"),
                                workOutPlan("Aerobics","clientHome")]
                )



package2=Packages("Gold",1500,4,"6 months",  [
    workOutPlan("yoga", "clientHome"),
    workOutPlan("cardio", "Trainer's place"),
    workOutPlan("weightloss", "clientHome"),
    workOutPlan("Aerobics", "clientHome")]
                  )
package3=Packages("Silver",800,3.5,"1 Year",[
    workOutPlan("yoga", "clientHome"),
    workOutPlan("cardio", "Trainer's place"),
    workOutPlan("weightloss", "clientHome"),
    workOutPlan("Aerobics", "clientHome")]

                )


package=[package1,package2,package3]

print(package)

for pack in package:
    pack.displayPackage()
