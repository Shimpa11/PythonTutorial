import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("confirmed.csv")

print(df.iloc[:,:6])
# table=pd.DataFrame(df,columns=['Province/State', 'Country', 'Lat', 'Long', 'Date22', 'Date23'])

# X=df['Country/Region']
# print(X)
# print(table)
# print(df.isnull())

# no of countries who have Nan value in ecjh col
# print(df.isnull().sum())
# hp=df.isnull().sum()
# print(hp)
dfk=df.keys()
# print(dfk)


# Converting all the integers i nto date time for better visualization
# print(df.head(10))


# f=df['1/22/20']=df['1/22/20'].astype('datetime64[ns]')
# print(f)
f=df.rename(columns={'1/22/20':'date22','1/23/20':'date23','1/24/20':'date24'
                     })
# print(f)
print(f.iloc[:, : 6])

gp=f.groupby(['Country/Region','date22'])
print(gp.groups)

x=f['Country/Region']
cols=df.keys()
confirmed=df.loc[:,cols[4]:cols[-1]]
dates=confirmed.keys()
sum_c=[]
for i in dates:
    y=confirmed_sum=confirmed[i].sum()
    sum_c.append(y)
print(sum_c)
countries=[]

countries=[countries for i in x]


# for i in x:
#     countries.append(i)

# print(x)
# print(y)
# countries=np.array([countries]).reshape(-1,1)
# sum_c=np.array([sum_c]).reshape(-1,1)


df.boxplot(countries,sum_c)


# plt.bar(countries,sum_c)
plt.xticks(rotation=40)

plt.show()
