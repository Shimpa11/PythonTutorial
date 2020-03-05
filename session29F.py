import re
import numpy as np
import matplotlib.pyplot as plt
list=['1.\n      Anand\n(1971)',
 '2.\n      Anbe \n(2003)',
]
print(list)



listToStr = ' '.join(map(str, list))
print(listToStr)


movies=[]
year=[]


s1=(re.findall(r"[A-Za-z]+", listToStr))
s2=(re.findall(r"[0-9]{4}", listToStr))

movies.append(s1)
year.append(s2)

print(movies)
print(year)




