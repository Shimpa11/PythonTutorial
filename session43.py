from sklearn import svm
"""
    Machine Learning
    Vehicles
    0 -> Bike
    1 -> Car
    Attributes : weight and engine
    weight      engine      vehicle
    Bikes:
    200kgs      100cc       0
    250kgs      200cc       0
    300kgs      300cc       0
    350kgs      350cc       0
    Cars:
    800kgs      800cc       1
    1000kgs     1100cc      1
    1200kgs     1300cc      1
    1500kgs     1550cc      1
"""

from sklearn import tree

# SUPERVISED MACHINE LEARNING :)
# CLASSIFICATION PROBLEM

# Representing Training Data

bike = 0
car = 1

bike1 = [200, 100]

X = [
        bike1, [250, 200], [300, 300], [350, 350],
        [800, 800], [1000, 1100], [1200, 1300], [1500, 1550]
    ]
Y = [bike, bike, bike, bike, car, car, car, car]

# Evaluation + Optimization

# Creating the Model


model=svm.SVC()
model.fit(X,Y)
vehicle=[1200,1100]
predictedVehicle=model.predict([vehicle])
print(predictedVehicle)
# always prefer model with higher accuracy, keeo testing the model for accuracy by changing them for datasets