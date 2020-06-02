"""Apriori Algorithm-> a data mining technique
process of identifying an assocaition between the items
assumes that any subset of a frequent itemset must be frequent

Dataset
TID  Cover   Guard  PowerBank Charger
1       1       1       1       1
2       1       0       1       1
3       0       0       1       1
4       0       1       0       0
5       1       1       1       1
6       1       1       0       1



# parameters for rule association
1. support
support(cover)=no of transactions in which cover apperaed/total transaction
                =4/6=0.66
2.Confidence  (x=>y)
confidence(cover, guard)-> powerbank
confidence(cover,guard,powerpbank)=
support(cover,guard, powerbank as bought together)/support(cover,guard)
 (2/6)/(3/6)=0.66

3.Lift
lift(x=>y) interestingness or likelihood of item y being purchaced when x is already sold
lift(cover, guard)=>{ poerbank}
customer purchasing powerbank  after cover and guard has been sold

support({cover, guard,powerbank})/support(cover)*support(guard)

2/6/4/6*4/6=0.77

if lift(x=>y)=1, no correlation, dont consider
            >1 ,postive correlation  likely to be bought
            <1 negative         unlikely to be bought
4. Conviction
conv(x=>y)=(1-support(y))/(1-confidence(x=>y)

conviction({cover, guard}=>{powerbank})=1-support(powerbank)/1-confidence(cover,gaurd)-> powerbank
(1-4/6)/1-0.66=1

if conv(x=>y)=1 ,    x has no realtion with y
                >1, positve

                more the value , higher the interesr of item being purchasecd

Frequency table for items
item        freq of occurence
Cover             4
Guard             4
PowerBank         4
Charger           5


 Assume Support as threshhold =3

 make pairs             Frequency
 Cover ,  Guard        3
 Cover.Powerbank       3
 Cover, Charger        4
 Guard, Powerbank      2
 Gurad, charger        3
 powerbank , Charger   4

  if Support threshold>3
  only 2 items pairs bought together
  Cover, Charger
  Powerbank and Charger


  we can  group in three's
  ( we can use various correlation)

"""
import  pandas as pd
from  apyori import apriori
df=pd.read_csv("transactions.csv",header=None)
# print(df)

# print(df.shape)

# # convert df as list of lists
records=[]
for i in range (df.shape[0]):
    # print(i)
    records.append([str(df.values[i,j])  for j in range(df.shape[1])])

# # apyori
# # list of lists
print(records)
associationRules = apriori(records, min_support=0.50,  min_confidence=0.7, min_lift=1, min_length=2)
print(list(associationRules))