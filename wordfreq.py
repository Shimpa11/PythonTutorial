import hashlib

class HashTable:

    # word = "institution"
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[]
        for i in range(capacity):
            self.table.append([])

    def hashCode(self,word):
        idx=(hashlib.sha256(word.encode("utf-8")).hexdigest(),16)
        # idx=hash(idex)%self.capacity
        return idx
        # print(idx)
    def put(self,word):

        idx=int(hashlib.sha256(word.encode("utf-8")).hexdigest(),16)%self.capacity
        if self.table[idx]==  None:

            self.size += 1

        else:
            print("collision")
        self.table[idx].append(word)
        # print(">> Data {} Inserted at Index {}".format(word, idx))

    # def find(self,word):
    #     idx = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) % self.capacity
    #     if self.table[idx]==word:
    #
    def iterate(self):
     for i in range(self.capacity):
        if len(self.table[i]) != 0:
            print(">> Data in BUCKET", i)

            for data in self.table[i]:
                print(data)
            print("---------------------------------")
    def count(self,word):
        self.frequency=0
        for i in range(self.capacity):
             for data in self.table[i]:
                if self.table[i]==word:
                    self.frequency=self.frequency+1
        print("the frequency is :",self.frequency)



# class Review:
#
#     def __init__(self,review=None):
#         self.review=review
#
#     def __str__(self):
#         return "{}\t{}\t{}".format(self.review)
# #     def show(self):
# #
# #
rev2=[]
review2 ="Best institution Education level is high"

rev=review2.split(" ")
for wd in rev:
    rev2.append(wd)
# print(rev2)

# reviews2=Review()
# reviews2.show()

review1 = """Really good institution teachers are very helpful and caring also
        environment of this college is very attractive Proud to be a part of this college"""

review2 = "Best institution Education level is high"

review3 = "What so ever I am today is due this technology Temple"
review4 =  "Nice place a big also it provides you good education"
review5 =  "Great institution with opportunities for those who want it"

rev5=[]
rev=review5.split(" ")
for wd in rev:
    rev5.append(wd)
# print(rev5)



hTable=HashTable(15)
hTable.put("hello")


# hTable.put(review1)
# hTable.put(review2)

# hTable.put(review3)
# hTable.put(review4)


# hTable.put(review5)
for r in rev2:
    hTable.put(r)



for r1 in rev5:
    hTable.put(r1)

print(hTable.table)
hTable.iterate()

for r in rev2:
    if r=="institution":
         hTable.count(r)





