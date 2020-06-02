import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as ncolors

# import seaborn as sns
import random
import math
import time
from sklearn.model_selection import RandomizedSearchCV,train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error,mean_absolute_error
import datetime
import operator
plt.style.use('seaborn')


# Loading all three datasets
confirmed_cases=pd.read_csv("confirmed.csv")
deaths_reported=pd.read_csv("deaths.csv")
recovered_cases=pd.read_csv("recovered.csv")

# Display the head of datasets
confirmed_cases.head()
deaths_reported.head()
recovered_cases.head()

# Extracting all the cols using .keys() function
cols=confirmed_cases.keys()
# print(cols)

# Extraction only dates cols that  have the data  for confirmed , deaths and recovered
confirmed=confirmed_cases.loc[:,cols[4]:cols[-1]]
deaths=deaths_reported.loc[:,cols[4]:cols[-1]]
recovered=recovered_cases.loc[:,cols[4]:cols[-1]]

# Check the head of outbreak cases
# print(confirmed.head())

# Finding total confirmed cases, death cases and recovered cases and append
# them to 4 empty list
#  total mortality rate= death_sum/confirmedcases

dates=confirmed.keys()
world_cases=[]
total_deaths=[]
mortality_rate=[]
total_recovered=[]

for i in dates:
    confirmed_sum=confirmed[i].sum()
    death_sum=deaths[i].sum()
    recovered_sum=recovered[i].sum()
    world_cases.append(confirmed_sum)
    total_deaths.append(death_sum)
    mortality_rate.append(death_sum/confirmed_sum)
    total_recovered.append(recovered_sum)


print("Total confirmed:",confirmed_sum)
print("Total deaths:",death_sum)
print("Total recovered:",recovered_sum)
print("Total world cases:",world_cases)
print("Total Mortality Rate:",mortality_rate)


#  Converting dates and cases  into numpy array

days_since_1_22=np.array([i for i in range(len(dates))])
world_cases=np.array(world_cases).reshape(-1,1)
total_deaths=np.array(total_deaths).reshape(-1,1)
total_recovered=np.array(total_recovered).reshape(-1,1)

print(days_since_1_22)
# print(world_cases)
# print(total_recovered)

# future forecasting for next 20Days
#  adding 10 more days to total
future_days=10
future_forecast=np.array([i for i in range(len(dates)+future_days)])
# print(future_forecast)
adjusted_days=future_forecast[: -10]
# print(adjusted_days)

# Converting all the integers i nto date time for better visualization
start='1/22/2020'
start_date=datetime.datetime.strptime(start,'%m/%d/%Y')
future_forecast_dates=[]
for i in range(len(future_forecast)):
    future_forecast_dates.append((start_date+datetime.timedelta(days=1)).strftime('%m/%d/%Y'))

# print(future_forecast_dates)

# For visualization with the latest data of 15 march
latest_confirmed=confirmed_cases[dates[-1]]
latest_deaths=deaths_reported[dates[-1]]
latest_recovered=recovered_cases[dates[-1]]
print(latest_confirmed)
# print(latest_deaths)
# print(latest_recovered)

# list of unique contries
unique_contries=list(confirmed_cases['Country/Region'].unique())
# print(unique_contries)

# total num of  confirmed cases for  each country
country_confirmed_cases=[]
no_cases=[]

for i in unique_contries:
    cases=latest_confirmed[confirmed_cases['Country/Region']==i].sum()
    if cases>0:
        country_confirmed_cases.append(cases)
    else:
        no_cases.append(i)
print("No cases countries:",no_cases)
print("Country with confirmed cases:",country_confirmed_cases)
#
# Find the cases per country

print(len(unique_contries))
print(len(country_confirmed_cases))
print(len(no_cases))
for i,j in zip(unique_contries,country_confirmed_cases):


    print( "country name",i ,": no of cases",j)



"""
process = [[1,2],[3,4],[5,6], [7,8,9]]

a = []
try:
    for thing in process:
        ds, ts = thing
        a.append((ds, ts))
except ValueError as e:
    print(e, '\t', thing)

"""
# List of uniques provinces
unique_provinces=list(confirmed_cases['Province/State'].unique())
# countries which are not provinces
print(unique_provinces)
# print(len(unique_provinces))
outliers=['South Australia','Queensland','Rockland County']
for i in outliers:
    # print(i)
    if i in unique_provinces:
        unique_provinces.remove(i)
print(len(unique_provinces))



# total num of  confirmed cases for  each province
province_confirmed_cases=[]
no_cases_p=[]

for i in unique_provinces:
    cases_province=latest_confirmed[confirmed_cases['Province/State']==i].sum()
    if cases>0:
        province_confirmed_cases.append(cases_province)
    else:
        no_cases_p.append(i)
# print("No cases provinces:",no_cases_p)
# print("Province with confirmed cases:",province_confirmed_cases)

# number of case per province
for i,j in zip(unique_provinces,province_confirmed_cases):


    print( "Province name",i ,": no of cases",j)


# Handling NAN value if any
nan_indices=[]
for i in range(len(unique_provinces)):
    if type(unique_provinces[i])==float:
        nan_indices.append(i)
unique_provinces=list(unique_provinces)
province_confirmed_cases=list(province_confirmed_cases)

for i in nan_indices:
    unique_provinces.pop(i)
    # province_confirmed_cases.pop(i)
    print(unique_provinces)

print(country_confirmed_cases)
print(len(country_confirmed_cases))
data=np.arange(len(unique_contries))
print(data)

# plt.figure(figsize=(32,32))
# plt.bar(confirmed_cases['Country/Region'],confirmed_cases)
# # plt.bar(data,country_confirmed_cases)
# plt.title("Number of covid-19 cases in Countries")
# plt.xlabel("Countries")
# plt.ylabel("Number of confirmed cases")
# # plt.xticks(data, unique_contries, fontsize=5, rotation=30)
#
# plt.show()


uc=pd.DataFrame(unique_contries,columns=['Countries'])
# print(uc)



cc=pd.DataFrame(country_confirmed_cases,columns=['No of confirmed cases'])


uc1=uc.append(cc)
# uc1=pd.merge(uc,cc)

# print(uc1)


# uc1.plot(kind='bar',x='Countries',y='No of confirmed cases',color='red')
# plt.xticks(rotation=40)
# plt.show()


# ax = sns.countplot(x='c', data=uc1['No of confirmed cases'])
#
# ax.set_xticklabels(ax.get_xticklabels(), fontsize=1)
# plt.tight_layout()
# plt.show()
#

china_confirmed=latest_confirmed[confirmed_cases['Country/Region']=='China'].sum()
out_mainland_china_confirmed=np.sum(country_confirmed_cases)-china_confirmed


print(china_confirmed)
print(out_mainland_china_confirmed)
plt.figure(figsize=(16,9))

# ax=sns.barplot(x=out_mainland_china_confirmed)
# # plt.bar(out_mainland_china_confirmed,y=country_confirmed_cases)
# ax=sns.barplot(x=china_confirmed)
# # plt.plot(china_confirmed)
# plt.title("number of confirmed cases for china")
# plt.show()


# only show 10 contries with most case and rest are grouped in category others
visual_unique_countries=[]
visual_confirmed_cases=[]
others=np.sum(country_confirmed_cases[110:])
for i in range(len(country_confirmed_cases[:10])):
    visual_unique_countries.append(unique_contries[i])
    visual_confirmed_cases.append(country_confirmed_cases[i])

visual_unique_countries.append('others')
visual_confirmed_cases.append(others)

plt.figure(figsize=(32,18))
plt.bar(visual_unique_countries,visual_confirmed_cases)
# sns.barplot(x=visual_confirmed_cases)
plt.title("First10 and others")
plt.show()


#create pie chart fot total confirmed cases in 10 different countries
# c=random.choices(list(ncolors.CSS4_COLORS.values()),k=len(unique_contries))
# plt.figure(figsize=(20,20))
# plt.title("cases per country")
# plt.pie(visual_confirmed_cases,colors=c)
# plt.legend(visual_unique_countries,loc='best')
# plt.show()

# create pie chart fot total confirmed cases in 10 different countries outside china
# c=random.choices(list(ncolors.CSS4_COLORS.values()),k=len(unique_contries))
# plt.figure(figsize=(20,20))
# plt.title("cases per country")
# plt.pie(visual_confirmed_cases[1:],colors=c)
# plt.legend(visual_unique_countries[1:],loc='best')
# plt.show()


# creating SVN Model
# kernel=['poly','sigmoid','rbf']
# c=[0.01,0.1,1,10]
# gamma=[0.01,0.1,1]
# epsilon=[0.01,0.1,1]
# shrinking=[True,False]
# svm_grid={'kernel':kernel,'c':c,'gamma':gamma,'epsilon':epsilon,'shrinking':shrinking}

X=np.array(confirmed_cases).reshape(-1,1)
Y=np.array(confirmed_cases).reshape(-1,1)
X_train_confirmed,Y_train_confirmed,x_test,y_test=train_test_split(X,Y,test_size=0.3,random_state=20)
# svm=SVR()
# svm_search=RandomizedSearchCV(svm,svm_grid,scoring='neg_mean_squared_error',cv=3,return_train_score=True,n_jobs=1,n_iter=40,verbose=1)
# svm_search.fit(X_train_confirmed,Y_train_confirmed)
# svm_search.best_params_
#
# svm_confirmed=svm_search.best_estimator_
# svm_pred=svm_confirmed.predict(future_forecast)
# print(svm_confirmed)
# print(svm_pred)
#
# # checking againg testing data
# svm_test_pred=svm_confirmed.predict(x_test)
# plt.plot(svm_test_pred)
# plt.plot(x_test)
# print(mean_absolute_error(svm_test_pred,y_test))
# print(mean_squared_error(svm_test_pred,y_test))



# total number of cases over the time
# plt.figure(figsize=(10,10))
# plt.plot(adjusted_days,world_cases)
# plt.title("total cases overthe time")
# plt.xlabel("daysSince1/22/202")
# plt.ylabel("number of cases")
# plt.xticks(size=15)
# plt.yticks(size=15)
# plt.show()

# confirmed vs predicted
# plt.figure(figsize=(10,10))
# plt.plot(adjusted_days,world_cases)
# plt.plot(future_forecast,svm_pred,linestyle='dashed',color='purple')
# plt.title("total cases overthe time")
# plt.xlabel("daysSince1/22/202")
# plt.ylabel("number of cases")
# plt.legend('confirmed cases','SVM Predictions')
# plt.xticks(size=15)
# plt.yticks(size=15)
# plt.show()


# prediction for next 10 days using svm
# print("SVM future predictions")
# set(zip(future_forecast_dates[-10:],svm_pred[-10:]))


# model linear regression for predictuion
from sklearn.linear_model import LinearRegression
linear_model=LinearRegression(normalize=True,fit_intercept=True)
linear_model.fit(X_train_confirmed,Y_train_confirmed)
linear_pred=linear_model.predict(future_forecast)
test_linear_pred=linear_model.predict(x_test)
print("MAE",mean_absolute_error(test_linear_pred,y_test))
print("MSE",mean_squared_error(test_linear_pred,y_test))

plt.plot(y_test)
plt.plot(test_linear_pred)


# plt.figure(figsize=(10,10))
# plt.plot(adjusted_days,world_cases)
# plt.plot(future_forecast,linear_pred,linestyle='dashed',color='orange')
# plt.title("total cases overthe time")
# plt.xlabel("daysSince1/22/202")
# plt.ylabel("number of cases")
# plt.xticks(size=15)
# plt.yticks(size=15)
# plt.show()


# prediction for next 10 days
print("Linear Regression future prediction")
print(linear_pred[-10:])



# total deaths
plt.figure(figsize=(10,10))
plt.plot(adjusted_days,total_deaths,color='red')
plt.title("total deaths over the time")
plt.xlabel("Time")
plt.ylabel("Number of deaths")
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()



mean_mortality_rate=np.mean(mortality_rate)
plt.figure(figsize=(10,10))
plt.plot(adjusted_days,mortality_rate,color='orange')
plt.axhline(y=mean_mortality_rate,linestyle='--',color='black')
plt.title("Mortality Rate")
plt.legend(['mortality rate','y='+str(mean_mortality_rate)])
plt.xlabel("Time")
plt.ylabel("Mortality Rate")
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()


# Recovered cases
plt.figure(figsize=(10,10))
plt.plot(adjusted_days,total_recovered,color='green')
plt.axhline(y=mean_mortality_rate,linestyle='--',color='black')
plt.title("Recovered cases")
plt.legend(['mortality rate','y='+str(mean_mortality_rate)])
plt.xlabel("Time")
plt.ylabel("Number of cases")
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()


# recovered vs deaths
plt.figure(figsize=(10,10))
plt.plot(adjusted_days,total_deaths,color='r')
plt.plot(adjusted_days,total_recovered,color='green')

plt.title("recovered vs deaths")
plt.legend(['deaths','recoveries'],loc='best')
plt.xlabel("Time")
plt.ylabel("Number of cases")
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()



plt.figure(figsize=(10,10))
plt.plot(total_recovered,total_deaths,color='r')
plt.plot(adjusted_days,total_recovered,color='green')

plt.title("recovered vs deaths")
plt.legend(['deaths','recoveries'],loc='best')
plt.xlabel("Recoveries")
plt.ylabel("deaths")
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()


"""

x= data.iloc[:, 0:2]
y= dataset.iloc[:, :-1]


"""
