import sklearn.datasets as datasets
import pandas as pd
iris=datasets.load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
y=iris.target


# Sklearn will generate a decision tree for your dataset using an optimized version of the CART algorithm when you run the following code.
from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree.fit(df,y)

#
# You can also import DecisionTreeRegressor from sklearn.tree if you want to
# use a decision tree to predict a numerical target variable. Try switching one
# of the columns of df with our y variable from above and fitting a regression tree on it.

# pydotplus package to create a visualization

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
from sklearn import tree
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

import pydotplus

# dot_data = StringIO()
# export_graphviz(dtree, out_file=dot_data,
#                 filled=True, rounded=True,
#                 special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())
data=tree.export_graphviz(dtree,out_file=None,feature_names=iris.feature_names, class_names=iris.target_names)

graph=graphviz.Source(data)
graph.render("IRIS DATASET DECISION TREE")
graph.view()