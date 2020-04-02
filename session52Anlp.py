import nltk
import requests
from bs4 import BeautifulSoup
url="https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"
response=requests.get(url)
print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
# some parsing in case needed

text=soup.text
# print(text)
# tokenization
tokens=[token for token in text.split()]
print(tokens)


# text preprocessing
from nltk.corpus import stopwords
# # list of stop words in english lib in nltk
stopWordRef=stopwords.words("english")
# print(stopWordRef)

tokensWithoutStopWords=tokens[:]

#  removing stopwords from tokens
for token in tokens:
    if token in stopWordRef:
        tokensWithoutStopWords.remove(token)

frequency=nltk.FreqDist(tokensWithoutStopWords)
frequency.plot(10)