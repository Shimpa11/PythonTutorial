"""Perceptron model to implement logical operations AND, OR


DECISION BOUNDARY
"""

import numpy as np

class Perceptron:

    def __init__(self):

    # # Assuming Weights: Pereptron as Logical AND
    #     self.weights = np.array([0.5, 0.5])

    # Assuming Weights: Pereptron as Logical OR
        self.weights = np.array([1.1, 1.1])

    # Weights may be assumed by hit and trial method to get our expected outputs
    # We can also manipulate threshold theta to get our expected outputs
    # We can even add an external input called bias to manipulate results as per our expectation

    #         assuming threshold
        self.theta=1
        print("Perceptron Created")

    def setInputs(self,inputs):
        self.inputs=inputs

    # sum of Inputs*Weifgts

    def summation(self):
        self.sum=np.dot(self.inputs,self.weights)
        print("Summation is ",self.sum)


    # Binary Step Activation Function
    def activation(self):
        if self.sum>=self.theta:
            return 1
        else:
            return 0




def main():
    # araay of inputs
    #               X1 X2
    input1=  np.array([0,0])
    input2 = np.array([0,1])
    input3 = np.array([1,0])
    input4 = np.array([1,1])


# create perceptron

    percepton=Perceptron()
    percepton.setInputs(input1)
    percepton.summation()
    print("For {} Result is : {}".format("0,0",percepton.activation()))

    percepton.setInputs(input2)
    percepton.summation()
    print("For {} Result is : {}".format("0,1", percepton.activation()))

    percepton.setInputs(input3)
    percepton.summation()
    print("For {} Result is : {}".format("1,0", percepton.activation()))

    percepton.setInputs(input4)
    percepton.summation()
    print("For {} Result is : {}".format("1,1", percepton.activation()))

if __name__=='__main__':
        main()