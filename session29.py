import matplotlib.pyplot as plt

# ages=[21,22.23,4,5,6,77,8,21,10,31,32,66,54,90]
# bins=5
# plt.hist(ages,bins)
# plt.hist(ages,5)  # 5 bins  data divided into 5 groups
# plt.show()

# languages=["python", "java","C++", "Dart","Javascript"]
# jobs=[70,80,88,12,90]
#
# # plt.bar(languages,jobs)
# # plot horizontally
# plt.barh(languages,jobs,align="center",alpha=0.3)
#
# plt.show()

years=[2015,2016,2017,2018,2019]
years1=[2015+0.30,2016+0.30,2017+0.30,2018+0.30,2019+0.30]


jobsInJava=[90,80,67,54,22]
jobsInPython=[80,70,55,60,19]
plt.bar(years,jobsInJava,width=0.3,color="b",label="Java")
plt.bar(years1,jobsInPython,width=0.3,color="g",label="Python")
plt.legend()
plt.show()
