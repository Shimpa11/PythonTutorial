"""
https://archive.ics.uci.edu/ml/datasets/seeds
https://en.wikipedia.org/wiki/Grain_quality#Wheat_quality
"""

# Coding ANN
import pandas as pd
import numpy as np
class DataSetHelper:
    def __init__(self):
        print("Preparing Dataset...")

    # func to read csv file and prepare X and Y
    #  prepare number of classes -> len(Y)
    #  can normalize data

    def readCSV(self,file,target,normalize=False):
        df=pd.read_csv(file)
        print(df)

        targetIndexes={target:idx for idx,target in enumerate(sorted(list(set(df[target].values))))}


        X=df.drop([target],axis=1).values
        print(X)

        Y=np.vectorize(lambda x:targetIndexes[x])(df[target].values)
        print(Y)

    #     classesa are dict keys
        classes=targetIndexes.keys()
        print(classes)

        numberOfClasses=len(targetIndexes)
        print(numberOfClasses)


        if normalize:
    #         Standardization
                X=(X-X.mean(axis=0))/X.std(axis=0)
        return X,Y,numberOfClasses


    # k fold validation
    #  randomly generating testing and training data
    #  Make data available for testing and training
    def kfoldCrossValidation(self,n,folds):
        np.random.seed(1)#seed is starting bumber from here randoms shall be generated
        indexes=np.random.permutation(n)

        nFold=int(n//folds)
        indexFolds=[]
        for i in range(folds):
            startIdx=i*nFold
            endIdx=min([(i+1)*nFold,n])
            indexFolds.append(indexes[startIdx:endIdx])

        return indexFolds


