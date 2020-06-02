import  matplotlib.pyplot as plt
languages=["Python", "Java","C++", "Dart","Javascript"]
jobs=[80,70,55,60,19]
# plt.pie(jobs,labels=languages)
plt.bar(languages,jobs)
plt.legend()
plt.show()
