# making # series  out of csv file usind data frame which is collection of series

import pandas as pd
table=pd.read_csv("cityTemps.csv")
print(table)

# fetching ony year
print(table["Year"])

print("==iloc=====")
# data of index3
print(table.iloc[3])

print("Slicing with iloc")
print(table.iloc[1:5])

print("Head")
print(table.head(5))

print("tail")
print(table.tail(5))