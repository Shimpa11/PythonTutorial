import pandas as pd

# Manual Creation of IPL Data Set
Teams = [
    "Rajasthan Royals",
    "Delhi Capitals",
    "Chennai Super Kings",
    "Delhi Capitals",
    "Mumbai Indians",
    "Kolkata Knight Riders",
    "Chennai Super Kings",
    "Deccan Chargers",
    "Kings XI Punjab",
    "Mumbai Indians",
]


Ranks = [2, 3, 4, 1, 3, 4, 1, 2, 5, 4]
Years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

iplData = {
    "Team": Teams,
    "Rank": Ranks,
    "Year": Years
}

anotherIplData = {
    "Team": ["Sunrisers Hyderabad", "Mumbai Indians", "Pune Warriors"],
    "Rank": [8, 9, 5],
    # "Year": [2015, 2019, 2018]
}

table1 = pd.DataFrame(iplData)
table2 = pd.DataFrame(anotherIplData)
print(table1)
print()
print(table2)
print()

# LEFT JOINS IN SQL
table3=pd.merge(table1,table2,on="Team",how="left")
# RIGHT JOIN
table3=pd.merge(table1,table2,on="Team",how="right")
# INNER JOIN
table3=pd.merge(table1,table2,on="Team",how="inner")
# OUTER JOIN
table3=pd.merge(table1,table2,on="Team",how="outer")

print(table3)