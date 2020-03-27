"""
    Unsupervised Learning
    We have data but no labels !!
    Classification will be numerically done by the model and we later name those classes
    Output is not known for observations in the dataset
    k-means clustering
    k here denotes number of classes we expect from model after classification
    ----------
    X   Y   P
    ----------
    1   1   A
    1   0   B
    0   2   C
    2   4   D
    3   5   E
    ----------
    we have above dataset as an example to work on 5 observations
    each observation has 2 data points
    But we don't know what class it belongs to




"""
"""
# we need to put data points mathematically
step1: Assumption of data points or centroids


no of data paoints is number of classes
K-represnts number of classes after classification
k-2, 2 datapoints
Assume any 2 datapoints randomly from the given dataset as CENTROIDS
egA(1,1) and C(0,2)

Step2:
calculate distance of each point from centroids
Eucilidean Distance formula
sqrt[square (x2-x1)+square(y2-y1)]

X  Y  P C1(1,1)  C2(0,2)
--------------------
1   1  A   0      1.4
1   0  B   1      2.2
0   2  C   1.4     0
2   4  D   3.2    2.8
3   5  E   4.5    4.2

Step3: Arrange points as per distance from centroids
P   nearest to
--------------------
A   C1
B   C1
C   C2
D   C2
E   C2
looking the data above A and B nearest to C! should be in One cluster
and C D and E  who are nearest to C2 should be in other cluster
Even now we dont know if above assumption is correct or not
we need to be sure about our assumption

Step 4:
so recheck again with new centroids and these
new centroids shall be mean of previous cluster

cluster 1 mean= mean of A nd B
cluster 2 mean= mean of C D and E data points

C1 Mean=(1+1)/2, (1+0)/2=(1,0.5)
C2  Mean=(0+2+3)/3,(2+4+5)/3=(1.7,3.7)


X  Y  P   C1 Mean       C2 Mean 
        distance(1,0.5)  distance(1.7,3.7)
         
--------------------
1   1  A   0.5    2.7
1   0  B   0.5     3.7
0   2  C   1.8     2.4
2   4  D   3.6     0.5
3   5  E   4.9     1.9

P   nearest to
--------------------
A   C1
B   C1
C   C1
D   C2
E   C2

one data point has been shifted from C2 to C1
still for surity , to hold it true
if we get the same result twice, we stop the futher computation
go on computing till we get the same result twice 

NC1=(1+1+0)/3,(1+0+2)/3=(0.7,1)
NC2=(2+3)/2,(4+5)/2=(2.5,4.5)


X  Y  P   NC1 Mean       NC2 Mean 
        distance(0.7,1)  distance(2.5,4.5)
         
--------------------
1   1  A   0.3      3.8
1   0  B   1.04     4.7
0   2  C   1.2     3.5
2   4  D   3.2      0
3   5  E   4.6    0.70


X  Y  P  nearest to
--------------------
1   1  A   C1
1   0  B   C1
0   2  C   C1
2   4  D   C2
3   5  E   C2

got the same  result
(0.7,1) class1
(2.5,4.5) class2



"""


import matplotlib.pyplot as plt
X=[1,1,0,2,3]
Y=[1,0,2,4,5]
plt.scatter(X,Y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.title("K-means Clustering")
plt.show()

class KMeans:
    def __init__(self,clusters=2):
        self.clusters=clusters
        print("KMeans Model Created")
    def fit(self,X,Y):
        pass
    def predict(self,X,Y):
        pass




