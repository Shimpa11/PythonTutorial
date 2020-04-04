import numpy as np
class PerceptonAND:

    def __init__(self):
        self.weights=np.array([0.5,0.5])
        self.theta=1
        print("Perceptron created for AND Operations")

    def summation(self):
        self.sum=np.dot(self.inputs, self.weights)
        print(self.sum)


    def activation(self):
        if self.sum>=self.theta:
            return 1
        else:
            return 0

    def processPerceptron(self,inputs):
        self.inputs=inputs
        self.summation()
        return self.activation()

class PerceptonNOT:

        def __init__(self):
            self.weight =-1
            self.theta = -0.5
            print("Perceptron created for OR Operations")

        def summation(self):
            self.sum = self.input*self.weight

        def activation(self):
            if self.sum >= self.theta:
                return 1
            else:
                return 0

        def processPerceptron(self,input):
            self.input = input
            self.summation()
            return self.activation()



def main():

#     array of inputs

    input1=np.array([0,0])
    input2=np.array([0,1])
    input3=np.array([1,0])
    input4=np.array([1,1])


    andPerceptron=PerceptonAND()
    notPerceptron=PerceptonNOT()


    and1=andPerceptron.processPerceptron(input1)
    and2 = andPerceptron.processPerceptron(input2)
    and3 = andPerceptron.processPerceptron(input3)
    and4 = andPerceptron.processPerceptron(input4)


    final1=notPerceptron.processPerceptron(and1)
    final2 = notPerceptron.processPerceptron(and2)
    final3 = notPerceptron.processPerceptron(and3)
    final4 = notPerceptron.processPerceptron(and4)

    # print(final1)
    # print(final2)
    # print(final3)
    # print(final4)


    print("Output for NAND Gate")
    print("NOT of ({} AND {}):  {}". format(input1[0],input1[1],  final1))
    print("NOT of ({} AND {}):  {}". format(input2[0], input2[1], final2))
    print("NOT of ({} AND {}):  {}".format(input3[0], input3[1], final3))
    print("NOT of ({} AND {}):  {}". format(input4[0], input3[1], final4))

if __name__=='__main__':
    main()
