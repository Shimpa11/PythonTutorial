""""
Feature Selection/ Dimensionality Reduction and feature Extraction

need to optimize our dataset with only those features which are meaningful
or contain more information

1.Variance Threshold->Quality of being difference
We shall remove all features./ attributes, whose variance doesnot meet the threshold specified by us

eg:We have a datset with features ans we wish to consider 80% of the sample



SelectKbest



"""
"""
from sklearn.feature_selection import VarianceThreshold
X=[
    [0,0,1],
    [0,0,1],
    [1,0,0],
    [1,1,1],
    [1,0,0],
    [0,1,0],
    [0,1,1]

]
print("X before")
print(X)
# Var[X]=p(1-p)-> p is threshold
reduction=VarianceThreshold(.8*(1-.8))
X=reduction.fit_transform(X)

print("X after")
print(X)
"""


from sklearn.feature_selection import VarianceThreshold

X = [
[0, 0, 1],
[0, 1, 0],
[1, 0, 0],
[0, 1, 1],
[0, 1, 0],
[0, 1, 1]
]

print("X BEFORE")
print(X)

# Var[X] = p(1-p)
reduction = VarianceThreshold(.8 * (1-.8))
X = reduction.fit_transform(X)

print("X AFTER")
print(X)

