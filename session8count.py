# data ="""work hard, get luckier.
# search the candle rather than cursing the darkness"""

# def count(data,word):
#     # c=0
#     j=0
#     for i in range(0, len(data)):
#         # for j in range(0,len(word)):
#             if data[i]==word:
#                 j=j+1
#
#         # c=c+1
#     return j
# data = "was the leader the string the variable"
# word = "r"
#
# print(count(data,word))


data = " the string the variable the set the list the tuple rather"
# data2=data.split(" , ")
words = ["the"]

def count(data,words):
    c=0
    for word in words:
        for i in range(0,len(data)):
            if data[i:i+len(word)]==word:
                c=c+1
            else:
                i=i+1
    return c

print("the occurs:",count(data,words))

# print("the " in data)




