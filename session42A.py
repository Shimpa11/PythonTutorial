import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
dataSet=pd.DataFrame()

dataSet['outlook']=['sunny','sunny','overcast','rainy','rainy','rainy',
                    'overcast','sunny','sunny','rainy','sunny',
                    'overcast','overcast','rainy']

# dataSet['temperature']=['hot','hot','hot','mild','cool',
#                       'cool','cool','mild','cool','mild',
#                         'mild','mild','hot','mild']
#
# dataSet['humidity']=['high','high','high','high','normal',
#                      'normal','normal','high','normal','normal','normal',
#                      'high','normal','high']
#
# dataSet['windy']=['false','true','false','false','false',
#                   'true','true','false','false','false','true','true',
#                   'false','true']

dataSet['play']=['no','no','yes','yes','yes','no',
                 'yes','no','yes','yes','yes','yes','yes','no']



print(dataSet)
print("====Fequency Table===========")
rainyDataset = dataSet[dataSet['outlook'] == 'rainy']
# print(rainyDataset)
print()

print("length of rainy dataset",len(rainyDataset))

print("yes_rainy",len(rainyDataset[rainyDataset['play'] == 'yes']))
print("no_rainy",len(rainyDataset[rainyDataset['play'] == 'no']))


print()

overcastDataset=dataSet[dataSet['outlook']=='overcast']
# print(overcastDataset)
print()
print("length of overcast",len(overcastDataset))
print("yes_overcast",len(overcastDataset[overcastDataset['play'] == 'yes']))
print("no_overcast", len(overcastDataset[overcastDataset['play'] == 'no']))

sunnyDataset = dataSet[dataSet['outlook'] == 'sunny']
# print(sunnyDataset)
print()
print("length of sunny dataset",len(sunnyDataset))
print("yes_sunny", len(sunnyDataset[sunnyDataset['play'] == 'yes']))
print("no_sunny", len(sunnyDataset[sunnyDataset['play'] == 'no']))


    # frequencyTable = pd.DataFrame()
    # frequencyTable['weather'] = ['overcast', 'rainy', 'sunny', 'grandTotal']
    # frequencyTable['No'] = [0, 3, 2, 5]
    # frequencyTable['yes'] = [4, 2, 3, 9]
    # print(frequencyTable)


    # sunnyDataFrame = dataset[dataset.outlook == "Sunny"]
    # sunnyTotal = len(sunnyDataFrame)
    # sunnyYes = len(sunnyDataFrame[dataset.play == "Yes"])
    # sunnyNo = len(sunnyDataFrame[dataset.play == "No"])
    # print("Sunny total :- {}, Yes :- {}, No :- {}".format(sunnyTotal, sunnyYes, sunnyNo))
    #
    # count = dataSet.groupby(['outlook', 'play']).size()
    # print(count,type(count))
print("==================")

print("likelyhood Table")
probabiltyOvercast=(len(overcastDataset[overcastDataset['play'] == 'yes'])+len(overcastDataset[overcastDataset['play'] == 'no']))/len(dataSet)
probabiltyRainy=(len(rainyDataset[rainyDataset['play'] == 'yes'])+len(rainyDataset[rainyDataset['play'] == 'no']))/len(dataSet)
probabiltySunny=(len(sunnyDataset[sunnyDataset['play'] == 'yes'])+len(sunnyDataset[sunnyDataset['play'] == 'no']))/len(dataSet)

print("probability of overcast",probabiltyOvercast)
print("probability of Rainy",probabiltyRainy)
print("probability of Sunny",probabiltySunny)

probabiltyAllYes=(len(overcastDataset[overcastDataset['play'] == 'yes'])+len(rainyDataset[rainyDataset['play'] == 'yes'])+
                                                                            len(sunnyDataset[sunnyDataset['play'] == 'yes']))/len(dataSet)
probabiltyAllNo=(len(overcastDataset[overcastDataset['play'] == 'no'])+len(rainyDataset[rainyDataset['play'] == 'no'])+
                                                                            len(sunnyDataset[sunnyDataset['play'] == 'no']))/len(dataSet)

print("ProbabilityYes",probabiltyAllYes)
print("ProbabiltyNo",probabiltyAllNo)

aYes=(len(overcastDataset[overcastDataset['play'] == 'yes'])+len(rainyDataset[rainyDataset['play'] == 'yes'])+
                                                                            len(sunnyDataset[sunnyDataset['play'] == 'yes']))


# prob(Yes|Sunny)=prob(Sunny|Yes)*prob(Yes)/prob(Sunny)
probSunnyYes=len(sunnyDataset[sunnyDataset['play'] == 'yes'])/aYes
print(probSunnyYes)
print()
probSunny=len(sunnyDataset)/len(dataSet)
print(probSunny)
print()
probYesSunny=probSunnyYes*probabiltyAllYes/probSunny
print(probYesSunny)


