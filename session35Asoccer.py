import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
table=pd.read_csv("soccerdata.csv")
print(table)
# by default first   5 rows
# print(table.head())
print(table["Name"])
# print(table.Name)


# g=table.head(100)
# sns.countplot(y=table.Nationality,palette="Set2")
# sns.countplot(y=table.Nationality,data=g,palette="Set2")

# sns.countplot(x="Age",data=table)
# sns.countplot(x="Nationality",data=table)
# plt.show()


# case study: find GK whos i sbest to stop the kicks

# create some weights
w1=1
w2=2
w3=3
w4=4
#
table["BEST_GK"]=(w1*table.GK_Kicking+w2*table.GK_Diving+w3*table.GK_Positioning+w4*table.GK_Reflexes)
print(table["BEST_GK"])
sortedData=table.sort_values("BEST_GK")
print(sortedData)

g1=sortedData.tail(10)

sns.countplot(x="Nationality",data=g1)
plt.xticks(rotation=90)
plt.show()


#
