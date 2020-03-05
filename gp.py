import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("IPL-TEAMS-DATA.csv",header=None)
print(data)

# table=pd.DataFrame(file,columns=["Index","Year","Team","M","W","L","T","N/R","PT","NRR",
#                                  "For","Against"])

data1=data.head(5)

team=data1[1]
wins=data1[3]

plt.bar(team,wins,"m")
plt.style.use(['dark_background'])
plt.xticks(rotation=90)
plt.show()