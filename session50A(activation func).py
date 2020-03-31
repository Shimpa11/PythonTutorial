import numpy as np
import matplotlib.pyplot as plt

# x=np.arange(-5,5)
# print(x)

# class Input:
#     def __init__(self,input,weight):
#         self.input=input
#         self.weight=weight


class Perceptron:

    def __init__(self,inputs):
        self.inputs=inputs
        print("Precepton created")

        print("=============")

    def summationFunction(self):
        self.sum=0
        for i in range (len(self.inputs)):

            self.sum+=self.inputs[i][0]*self.inputs[i][1]

        print("summation Function output", self.sum)

    # def activationFunctionSigmoid(self):
    #     self.sigm=0
    #
    #
    #     self.sigm=1/(1+np.exp(self.sum))
    #
    #     print("output is ",self.sigm)
    #     if 0<self.sigm<1:
    #         print("Decision Taken")
    #     else:
    #     #     print("output is 0")
    #         print("Decision  not Taken")


#Linear Transform f(x)=x, input is the summation fn

    # def activationFunctionLinear(self):
    #     output=self.sum
    #     if output==self.sum:
    #         print("output is ",output)
    #         print("Decision taken")
    #     else:
    #         print("Decision not taken")
    #

    # def activationFunctionUnitStep(self):
    #
    #     if self.sum>=0:
    #         print("output is ", 1)
    #         print("Decision taken")
    #     else:
    #         print("Decision not taken")

    def activationFunctionTanh(self):
        self.tanhyper=0
        self.tanhyper=np.tanh(self.sum)

        if 0<self.tanhyper < 1:
            print("output is ", self.tanhyper)
            print("Decision taken")
        else:
            print("Decision not taken")

    def activationRectified(self,x):
        # if x > 0:
        #     print(x)
        #
        #     print("decision taken and output is",x)
        # else:
        #     return 0
        print( max(0.0,x))

   # define a series of inputs



# rectified linear function





def main():

    # list of lists as input and weight, x0 w0, x1,w1....
    # [input weight]
    inputs=[
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]

    print(inputs)
    perceptron=Perceptron(inputs)
    perceptron.summationFunction()
    perceptron.activationRectified(5)
    # perceptron.activationFunctionSigmoid()
    # perceptron.activationFunctionLinear()
    # perceptron.activationFunctionUnitStep()
    # perceptron.activationFunctionTanh()
# series_in = [x for x in range(-10, 11)]
#         # calculate outputs for our inputs
# series_out = perceptron.activationRectified(x) for x in series_in:
#     # line plot of raw inputs to rectified outputs
# plt.plot(series_in, series_out)
# plt.show()


if __name__=='__main__':
    main()
