"""
Natural Language Processing
 Significant and actionable insight from unstructured textual data
getting some thing out of textual data

structure data set- csv files, tables, databases,organised data, eg dict , objects
unstructured -> 20% is only structure
eg text messages, comments, reviews
unstructured data cannot be used by ML

NLP part of CS and AI
branch of DS analysing  understanding  and extracting data

Machine translation
Automatic Summarization

NER
relationship Extraction
sentiment analysis
speech Recognition eg siri, chatbot
Topic segmentation

Tokenization: process of conveting text into tokens(words)
text object sentence phrase or word or article

break the sentence into words
importance of words
produce structured description


Text preprocessing
cleaning and standarization of text
noise removal -> any unuseful info, not relevant to the context of data
  is noise
lexicon normalization-> multiple representations exhin=bited by single word
stemming-> ing, ly, es,s , ect
lemmatization-> reaching to root word
object standariztion



"""

"""

import requests
from bs4 import BeautifulSoup
url="https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"
response=requests.get(url)
print(response.text)
"""


# Text Preprocessing- 1. Noise Removal
stopWords=["is","are","an", "the","am","...","to","a","and"]
def removeNoiseFromText(text):
    words=text.split()
    print(words)
    noiseFreeWords=[word for word in words if word not in stopWords]
    print(noiseFreeWords)
    noiseFreeText=" ".join(noiseFreeWords)
    return noiseFreeText


text="I am really happy and we are going to a vacation"
noiseFreeText=removeNoiseFromText(text)
print(noiseFreeText)

print("===================================")

import re

def removeNoiseFromTextWithRegEx(text,regExPattern):
    matches=re.finditer(regExPattern,text)
    print(matches)
    for match in matches:
        # print(match)
        print(match.group())
        text=re.sub(match.group().strip(), '',text)
    return text


text="Stay at home #covid19.Stay safe"
regExPattern="#[\w]*"
noiseFreeText=removeNoiseFromTextWithRegEx(text,regExPattern)
print(noiseFreeText)


import nltk
# ->  just for one time downloading with GUI
# nltk.download()

 # downloading eith command
nltk.download(stopWords)

# working with stemmimng and lemmatization

# stemmimg ->removing ing, es s etc
from nltk.stem.porter import PorterStemmer
stem=PorterStemmer()
word="races"
print(stem.stem(word))

# lemmatization-> getting root word
from nltk.stem.wordnet import WordNetLemmatizer
lem=WordNetLemmatizer()
word="multiplying"
print(lem.lemmatize(word,"v"))

# object Standarization
#  some slangs, some words not available  in dictionary , hashtags
# create our own std dict

dictionary={ "brb": "be right back",
                   "cb": "call back",
                   "awsm": " awesome",
                   "lol": "laugh out loud"
                   }
print(dictionary)


def objectStandarization(text):
    words=text.split()
    substitutedWords=[]
    for word in words:
        if word in dictionary:
             word=dictionary[word]
        substitutedWords.append(word)

    text=" ".join(substitutedWords)
    return text
text=" awsm you are. cb me soon"
print(objectStandarization(text))

# parts of speech Tagging-> autocorrection
# some nouns, adverbs, adjectivs, verb-> representing with tags
# with the help of pos tags

from nltk import word_tokenize,pos_tag

sentence="Stay safe. Be at home. Learn well and code regularly"

# converting sentence into tokens or single words
tokens=word_tokenize(sentence)

# print pos tags
print(pos_tag(tokens))