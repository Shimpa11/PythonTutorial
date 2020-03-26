from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
# vehicle classification :Weighr , Engine
trainingData=[
    [100,100],
    [150,110],
    [180,150],
    [200,180],
    [800,1000],
    [1000,1200],
    [1200,1300],
    [1500,1500],
]
# Labels
bike=0
car=1
# trainingLabels=[0,0,0,0,1,1,1,1]
trainingLabels=[bike,bike,bike,bike,car,car,car,car]
labelNames=["Bike","Car"]

testingData=[
    [110,105],
    [1011,1101],
    [190,160],
    [911, 1213],
    [160,90],
    [220,170],
    [1397,1260],
    [1475,1300]

]
# consider three nearest datapoints to perform predictions
model=KNeighborsClassifier(n_neighbors=3)
model.fit(trainingData,trainingLabels)

# sampleInput=[213,110]
# predictedClass=model.predict([sampleInput])
# print(labelNames[predictedClass[0]])

predictedClasses=model.predict(testingData)
print(predictedClasses)
# solve using digit dataset from sklearn
# solve regression problem using covid 19  dataset


