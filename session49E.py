from sklearn.feature_extraction.text import CountVectorizer
countVec=CountVectorizer()
print(countVec)
sentences= [
    'This is the first Algorithm'
    'This is the Second Algorithm'
    'This is the Third Algorithm'
]
print(sentences)

X=countVec.fit_transform(sentences)
print(X)

analysis=countVec.build_analyzer()
print(analysis)

print(countVec.get_feature_names())
print(X.toarray())