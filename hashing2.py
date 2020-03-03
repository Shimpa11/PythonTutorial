
class HashTable:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.size=0
        self.table=[]
        for i in range(capacity):
            self.table.append([])

    def hashCode(self, data):
        idx = id(data) % self.capacity

        return idx

    def put(self, data):
        idx = self.hashCode(data)
        # if self.table[idx]==None:
        self.table[idx].append(data)
        print(">> Data {} Inserted at Index {}".format(data, idx))
        self.size += 1
        # else:
        #     print("collision detected")

    def find(self,data):
        idx=self.hashCode(data)
        for data in self.table[idx]:
            if len(self.table)!=None:

                print("data at  index {} is".format(idx),data)
            else:
                print("Data not found")
    def delete(self,data):
        idx=self.hashCode(data)
        for data in self.table[idx]:
            if self.table[idx]==data:

                self.table[idx]=None
                self.size-=1
            print("Data deleted at index {}".format(idx),data)



    def iterate(self):
        for i in range(self.capacity):
            if len(self.table[i]) != 0:
                print(">> Data in BUCKET", i)

                for data in self.table[i]:
                    print(data)

                print("~~~~~~~~~~~~~~")

    def show(self,data):
        for data in self.table:
            if len(self.table)!=None:
                 print(data)