"""
Named entity recognition (NER)
Given a stream of text, determine
which items in the text map to proper names, such as people or places, and what the type of  each such name is (e.g. person, location, organization).
  Although capitalization can aid in recognizing named    entities in languages such as English, this
   information cannot aid in determining the type of    named entity, and in any case, is often inaccurate
    or insufficient. For example, the first letter     of a sentence is also capitalized, and named
     entities often span several words, only some of which are capitalized. Furthermore,
     many other languages in non-Western scripts (e.g. Chinese or Arabic) do not have any capitalization at all, and even languages
      with capitalization may not consistently use it to distinguish names. For example, German capitalizes all nouns, regardless of whether they are
      names, and French and Spanish do not capitalize names that serve as adjectives.

"""
from nltk import ne_chunk
from nltk import word_tokenize,pos_tag

# text="The US president lives in WhiteHouse"
# ne_tokens=word_tokenize(text)
# print(ne_tokens)
# print()
#
# ne_tags=pos_tag(ne_tokens)
# print(ne_tags)
# print()
#
# ne_NER=ne_chunk(ne_tags)
# print(ne_NER)

"""
 SYNTAX-> REFER TO STUDY PRINCIPLES AND RULES PROCESS
  THAT FORMS THE STRUCTURE OF A SENTENCE..
  SYNTAX  TREE-> REP OF SYNTACTIC STRUC OF SENTENCES OR STRINGS


CHUNKING
The process of classifying words into
 their parts of speech and labeling them accordingly 
 is known as part-of-speech tagging, POS-tagging, or simply tagging. Parts of speech
  are also known as word classes or lexical categories. The collection of tags used 
for a particular task is known as a tagset.



"""
# text1=" the big cat ate the litte mouse who was after the fresh cheese"
#
# c_tokens=word_tokenize(text1)
# c_tags=pos_tag(c_tokens)
# print(list(c_tags))
# from nltk import RegexpParser
# from nltk import ne_chunk
# grammer_np=r"NP:{<DT>? <JJ>?<NN>}"
# chunk_parser=RegexpParser(grammer_np)
# chunk_result=chunk_parser.parse(c_tags)
# print(chunk_result)



import os
import nltk
# nltk.download()
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
print(os.listdir(nltk.data.find("corpura")))

from nltk.corpus import movie_reviews
print(movie_reviews.categories())
print(len(movie_reviews.fileids('pos')))


