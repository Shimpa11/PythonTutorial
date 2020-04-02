import nltk
import nltk.corpus
import os
# print(os.listdir(nltk.data.find("corpora")))

AI="""Artificial intelligence (AI), also known as machine intelligence, is a branch of computer science 
   that aims to imbue software with the ability to analyze its environment using either predetermined rules 
   and search algorithms, or pattern  recognizing machine learning models, and    
   then make decisions based on those analyses."""

type(AI)

from nltk.tokenize import word_tokenize
# list of words and  special characters
# AI_tokens=word_tokenize(AI)
# print(AI_tokens,"\n",len(AI_tokens))



# tokens=[token for token in AI.split()]
tokens=word_tokenize(AI)

print(tokens)


# freq of distinct elements

from nltk.probability import FreqDist

fDist=FreqDist()
for word in tokens:
    fDist[word.lower()]+=1
print(fDist ,"\n")
# fDist.plot(10)

# frequency=nltk.FreqDist(AI_tokens)
# print(frequency)

# blank tokenizer
from nltk.tokenize import blankline_tokenize
AI_blank=blankline_tokenize(AI)
print(len(AI_blank))

# bigrams tigrams,  ngrams
# token of two, three  N consecutive written words

from nltk.util import bigrams,trigrams,ngrams
string="the best thing in the world cannot be seen and only be felt"
strTokens=word_tokenize(string)
print(list(strTokens))

# bigrams
strBigrams=list(nltk.bigrams(strTokens))
# print(strBigrams)

# trigrams
strTrigrams=list(nltk.trigrams(strTokens))
# print(strTrigrams)

# ngrams
strNgrams=list(nltk.ngrams(strTokens,4))
# print(strNgrams)

# Stemming-> root word cutting end or beginning of the word,
#   result may not be  exact word
#  types of stems

from nltk.stem import  PorterStemmer
pst=PorterStemmer()
print(pst.stem("having"))
print()
wordToStem=["give", "given", "giving","gave"]

for word in wordToStem:
    print(pst.stem(word))
print()

#  more aggressive approach
from nltk.stem import LancasterStemmer
lst=LancasterStemmer()

word="better"
#  how many giv words appear in the text
print(lst.stem(word))
print()
for word in wordToStem:
    print(lst.stem(word))
print()

print()

# Lemmatization

# groups together different inflected froms of a word called Lemma,
#  maps several words into one common  actual root word
#  proper  word
#   gone , going, went    into  Go  actual root word

from nltk.stem import wordnet

from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
#  lemmatizer requires   a detailed dictionary as output is a proper word , so wordnet is required
word_len=WordNetLemmatizer()


wlem=word_len.lemmatize("better")


print(pos_tag(wlem))

print()

for word in wordToStem:
    print(word_len.lemmatize(word))
print()


#  Pos tags -> parts of speech, noun verb , adj , conjuction, preposition
from nltk import pos_tag

text1="The ultimate objective of (NLP) is to #read, #decipher, understand! and make sense of the human languages in a manner that is valuable."

for word in text1:
    tk=word_tokenize(text1)
print(tk)



from nltk.corpus import stopwords
# stopwords
#  for processing not important but  useful for formation of sentence, cannot be completed
sw=stopwords.words("english")
# print(sw)
# print(len(sw))
#
import re
#  removing stopwords
punctuation=re.compile(r'[-,? !.: ;() # 0-9]')
post_punctuation=[]
for word in tk:
    word=punctuation.sub(" ",word)
    if len(word)>0:
        post_punctuation.append(word)

print(post_punctuation)

print(len(post_punctuation))




"""

A stemmer will return the stem of a word, which needn't be identical to the morphological root of the word. It usually sufficient that related words map to the same stem,even if the stem is not in itself a valid root, while in lemmatisation, it will return the dictionary form of a word, which must be a valid word.

In lemmatisation, the part of speech of a word should be first determined and the normalisation rules will be different for different part of speech, while the stemmer operates on a single word without knowledge of the context, and therefore cannot discriminate between words which have different meanings depending on part of speech.
"""

#
