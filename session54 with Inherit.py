# https://www.geeksforgeeks.org/effect-of-bias-in-neural-network/
# Perceptron foR XOR LOGICAL GATE

"""
XOR
A B Y
0 0 0
0 1 1
1 0 1
1 1 0

AND OR NOT , REST ALL OPERATONS MUST BE DERIVED FROM ABOVE
A XOR B=   (A OR B ) AND (NOT(A AND B))
A:0 B:0
0 OR 0  AND NOT ( 0 AND 0)
0 AND NOT 0
0 AND 1= 0
SAME FOR ALL OTHER INPUTS
A:0 B;1
0 OR 1 AND NOT ( 0 AND 1)
1 AND NOT (0)
1 AND 1
1

A:1 B;0
1 OR 0 AND NOT ( 1 AND 0)
1 AND NOT (0)
1 AND 1
1

A:1 B;1
1 OR 1 AND NOT ( 1 AND 1)
1 AND NOT (1)
1 AND 0
0

#  4 percepetron
"""
# for OR OPERATION
import numpy as np


# import struct
# print(struct.calcsize("P") * 8)

class Perceptron:
    def __init__(self,inputs):
          self.inputs=inputs
         # self.theta=theta
         # self.weights=weights


    def summation(self):

        self.sum = np.dot(self.inputs, self.weights)
        print(self.sum)

    # Binary Step Activation Function
    def activation(self):
        if self.sum >= self.theta:
         return 1
        else:
            return 0

    def processPerceptron(self, inputs):
        self.inputs = inputs
        self.summation()
        return self.activation()


class PerceptronOR(Perceptron):
        def __init__(self,theta,weights):

             # Perceptron.__init__(self,inputs)
             self.weights=weights
             self.theta=theta

             # self.weights = np.array([1.1, 1.1])
             # Perceptron.theta = 1

        print(">> Perceptron1 Created for OR Operations")


        # sumOR=Perceptron.summation(sum)



# # AND Operation
# class PerceptronAND(Perceptron):
#
#     def __init__(self,inputs,theta,weights):
#         Perceptron.__init__(self,inputs)
#         self.weights = np.array([0.5, 0.5])
#         self.theta = 1
#
#         print(">> Perceptron2 Created for AND Operations")

#

# NOT Operation
# class PerceptronNOT:
#
#     def __init__(self):
#
#         self.weight = -1
#         self.theta = -0.5
#         print(">> Perceptron3 Created for NOT Operations")
#
#     # Sum of Inputs*Weights
#     def summation(self):
#         self.sum = self.input * self.weight
# # print(">> summation is:", self.sum)
#
# # Binary Step Activation Function
#     def activation(self):
#         if self.sum >= self.theta:
#             return 1
#         else:
#             return 0
#
#     def processPerceptron(self, input):
#             self.input = input
#             self.summation()
#             return self.activation()

def main():
    # array of inputs
    #                  A  B
    input1 = np.array([0, 0])
    input2 = np.array([0, 1])
    input3 = np.array([1, 0])
    input4 = np.array([1, 1])

    # orPerceptron=Perceptron(input1)

    orPerceptron1=PerceptronOR(np.array([0.5,0.5]),1)

    orPerceptron1.processPerceptron(input1)
    # orPerceptron1.activation()


    # andPerceptron=PerceptronAND()
    # notPerceptron=PerceptronNOT()

    # A OR B OPERATION
    or1 = orPerceptron1.processPerceptron()
    # or2 = orPerceptron.processPerceptron(input2)
    # or3 = orPerceptron.processPerceptron(input3)
    # or4 = orPerceptron.processPerceptron(input4)

    # A AND B  OPERATION
    # and1 = andPerceptron.processPerceptron(input1)
    # and2 = andPerceptron.processPerceptron(input2)
    # and3 = andPerceptron.processPerceptron(input3)
    # and4 = andPerceptron.processPerceptron(input4)


    # NOT( A AND B)

    # not1 = notPerceptron.processPerceptron(and1)
    # not2 = notPerceptron.processPerceptron(and2)
    # not3 = notPerceptron.processPerceptron(and3)
    # not4 = notPerceptron.processPerceptron(and4)

    print(or1)

    # # ( A OR B ) AND ( NOT (A AND B) )
    # finalInput1 = np.array([or1, not1])
    # final1 = andPerceptron.processPerceptron(finalInput1)
    # final2 = andPerceptron.processPerceptron(np.array([or2, not2]))
    # final3 = andPerceptron.processPerceptron(np.array([or3, not3]))
    # final4 = andPerceptron.processPerceptron(np.array([or4, not4]))

    # # A XOR B  # XOR OPERATION
    #     print("( {} OR {} ) AND (NOT ({} AND {})) :  {}".format(input1[0], input1[1], input1[0], input1[1], final1))
    #     print("( {} OR {} ) AND ( NOT ({} AND {}))  : {}".format(input2[0], input2[1], input2[0], input2[1], final2))
    #     print("( {} OR {} ) AND ( NOT ({} AND {}) ) : {}".format(input3[0], input3[1], input3[0], input3[1], final3))
    #     print("( {} OR {} ) AND ( NOT ({} AND {}) ) : {}".format(input4[0], input4[1], input4[0], input4[1], final4))

if __name__ == '__main__':
        main()



"""
PL- Python
DB connectivity- SQL/NOSQL
                    MySQL/ FIREBASEFIRESTOR

GUI Development for desktop apps

how data can be collected in DB through a software

marks of every exam conducted for a student
pateient details along with medicines problems blood reports
CA  details of client and data wrt accounts for the client
Agricultural Companny
seeds, insecticides, pesticides , fungicides
crop details , insects, pest medicine, problems

Hospitality
hotel, restaurant
customer details, type of food the customer has ordered
App
Insert/update/ retreive/ Delete

GUI part
tkinter- desktop based
flask- web based

from our app we will be able to collect data and read to form csv files i.e. datasets
=================================================================

Web scraping and dataset generation
from web pages collect data and read  to form csv files i,e datasets

eg on amazon flipkart reading reviews and generating datasets

Project
Module 1  Dataset Generation
Module 2: implemnt ML problem statements
        1.Regression (value prediction)
            sklearn - a normal model
            tensorflow- ann model
        2. Classification(Image)
        pytorch/ tensorflow---
        Implementing these problem statemnts in ANN

amt of bill  and predicting next bill
insects  weather and predicting medicines



classification
classify faces of students 
crops images insects images

patients faces detect and telling medicines for next month
balnace sheet scan pytessaet , data analysis
number of vehicles parked
bike and cars numbers

dataset generation 5 days
regression 2 days/ 6 hours a day
classification 3 days 

google colabs 
incase tensorflow/ pytorch not working

AI- researh work | innovation

topic
app+db+dataset/ webscrapping +dataset
> App+DataBase+dataSet / WebScrapping+DataSet
	  How is your dataset and what will be the attributes in the data set
	> Images in Your Project  



recording into text 
and finding number of occurence of a word

analyse reviews and content on website
analyse linkedin profiles
python program
detecting 2 and 4 wheeler
number plate detection'
 whch vehicle is travelling here and there
 on the basis of whci we can predict fuel consumption
 
"""




