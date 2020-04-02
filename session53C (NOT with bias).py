#Perceptron with logical NOT  With bias

import numpy as np
class Perceptron:
    def __init__(self):
        # Assume weight
        self.weight=-2

        # Assume threshold
        self.theta=0.5
        print("Perceptron Created")

    def setInputs(self,input):
        self.input=input

    def summation(self,bias):
        self.sum=np.dot(self.input, self.weight)+bias
        print("summation is:",self.sum)

    def activation(self):
        if self.sum>=self.theta:
            return 1
        else:
            return 0


def main():
#     create perceptron
    perceptron=Perceptron()

    # bias
    bias=2
    # set inputs
    perceptron.setInputs(input=0)
    perceptron.summation(bias)
    print("For {}, Result is: {}".format("0",perceptron.activation()))

    perceptron.setInputs(input=1)
    perceptron.summation(bias)
    print("For {}, Result is: {}".format("1",perceptron.activation()))



if __name__ == '__main__':
    main()


