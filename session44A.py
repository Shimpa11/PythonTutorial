from sklearn import svm

from sklearn.cluster import KMeans
"""
    Machine Learning
   
    Attributes : weight and engine
    
    weight      engine      
    Bikes:
    200kgs      100cc       
    250kgs      200cc       
    300kgs      300cc       
    350kgs      350cc       
    
    Cars:
    800kgs      800cc       
    1000kgs     1100cc      
    1200kgs     1300cc      
    1500kgs     1550cc      
"""



# UNSUPERVISED MACHINE LEARNING :)
# CLASSIFICATION PROBLEM

# Representing Training Data



bike1 = [200, 100]
car1=[800,800]
data = [
        bike1, [250, 200], [300, 300], [350, 350],
        [800, 800], [1000, 1100], [1200, 1300], [1500, 1550]
    ]
targetNames = ["Car", "Bike"]

# Evaluation + Optimization

# Creating the Model

clusters=2
model=KMeans(n_clusters=clusters)
# Train the Model but no labels specified
model.fit(data)



# predictions = model.predict(data)
# print(predictions)


vehicle=[350,350]
predictedVehicle=model.predict([vehicle])
print(predictedVehicle)
print(targetNames[predictedVehicle[0]])
# always prefer model with higher accuracy, keeo testing the model for accuracy by changing them for datasets
