import pandas as pd
import math

def euclideanDistance(point1,point2):
    sumOfSquaredDistance = 0
    for i in range(len(point1)):
        sumOfSquaredDistance+=math.pow(point1[i]-point2[i],2)
    return math.sqrt((sumOfSquaredDistance))

def main():

    dataSet=[[65.2, 120.22],[71.5, 35.77],[69.8, 153.23],[67.2, 148.55],
                [68.5, 133.11],[69.11, 148.5],[70.55, 160.0], [67.33, 112.9], [66.49, 127.11]]

#     predict the value of weight given value height
    givenHeight=[60]
    # with KNN solve regression problem
    k=3
    # list in which we will place distance of the data points from the givenheight
    neighborDistances=[]
    for idx,dataPoint in enumerate(dataSet):
        print(idx,dataPoint)
        # compute distance of each datapoint from given heoight
        distance=euclideanDistance(dataPoint[:-1],givenHeight)

        print("distancebetween {} and {} is {}".format(dataPoint[:-1],givenHeight,distance))

        neighborDistances.append((distance,idx))
        #sort the list in acending order based on distance
    neighborDistances=sorted(neighborDistances)
    print(neighborDistances)


            # pic first k datapoint from sorted list
    kNearestNeighbors=neighborDistances[:k]
    print("K Nearest Neighbors")
    print(kNearestNeighbors)
        # since its a regression problem, compute mean of the labels
    outputLabels=[]
    for neighbor in kNearestNeighbors:
            print(neighbor)
            # neighbor[1] is index
            # outputLabels.append(dataSet[neighbor[1]][1])
            idx=neighbor[1]
            outputLabels.append(dataSet[idx][1])
            predictedweight=sum(outputLabels)/len(outputLabels)
    print(predictedweight)


if' __name__==main__':
    main()