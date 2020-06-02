import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as ncolors

import seaborn as sns
plt.style.use('seaborn')

confirmed_cases=pd.read_csv("confirmed.csv")
# print(confirmed_cases)

confirmed_cases['Province/State']=confirmed_cases.fillna("None",inplace=True)
print(confirmed_cases)
unique_contries=list(confirmed_cases['Country/Region'].unique())
print(unique_contries)
print(len(unique_contries))

cols=confirmed_cases.keys()

confirmed=confirmed_cases.loc[:,cols[4]:cols[-1]]
dates=confirmed.keys()

latest_confirmed=confirmed_cases[dates[-1]]
country_confirmed_cases=[]
no_cases=[]

for i in unique_contries:
    cases=latest_confirmed[confirmed_cases['Country/Region']==i].sum()
    if cases>0:
        country_confirmed_cases.append(cases)
    else:
        no_cases.append(i)

for n in range(len(country_confirmed_cases), 10):
    country_confirmed_cases.append(str(0))


print(type(country_confirmed_cases))


print(len(country_confirmed_cases))

# added_days=10
# future_forecast=np.array([i for i in range(len(country_confirmed_cases)+added_days)])
# print(len(future_forecast))
#
#
# plt.plot(unique_contries,country_confirmed_cases)
# plt.show()