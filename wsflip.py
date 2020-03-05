import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url="https://www.myntra.com/men-kurtas?p=2"
response=requests.get(url)
# print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

tagAll=soup.find_all("div", class_="product-sizeDisplayHeader")
for tag in tagAll:
    # print(tag.text)
