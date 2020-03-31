# class Input:
#     def __init__(self,input,weight):
#         self.input=input
#         self.weight=weight


class Perceptron:

    def __init__(self,inputs):
        self.inputs=inputs
        print("Precepton created")
        print(inputs)
        print("=============")

    def summationFunction(self):
        self.sum=0
        for i in range (len(self.inputs)):
            self.sum+=self.inputs[i][0]*self.inputs[i][1]
        print("summation Function output",self.sum)

    def activationFunction(self):
        threshold=1
        if self.sum>=threshold:
            print("output is 1")
            print("Decision Taken")
        else:
            print("output is 0")
            print("Decision  not Taken")


#Linear Transform f(x)=x, input is the summation fn



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
    perceptron.activationFunction()


if __name__=='__main__':
    main()