#  executing ANN from here

from session58A import ANN
from session58backprop import DataSetHelper

def main():

    fileName = "seeds.csv"

    dsHelper = DataSetHelper()

    X, Y, numOfClasses = dsHelper.readCSVFile(file=fileName, target="y", noramlize=True)

    print(X)
    print(Y)
    print(numOfClasses)




if __name__ == '__main__':
    main()

