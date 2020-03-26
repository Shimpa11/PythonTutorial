# graph data structure
#https://visualgo.net/en/graphds

# bidirectional or undirected graph nodes bidirection ,path is considedred in one dir only
# G(V,E)| V is vertices/nodes and E is edges

# adjcent nodes


class User:
    def __init__(self,uid,name,phone,email):
        self.uid=uid
        self.name=name
        self.phone=phone
        self.email=email
    def getUserDetails(self):
        return "{}|{}|{}|{}".format(self.uid,self.name,self.phone,self.email)

class FaceBookGraph:
    def __init__(self):
        self.users=dict()
        print("Facebook Graph created and users are ",self.users, "and size",len(self.users))

    #  add vertex

    def registeredUser(self,user):
        self.users[user]=[] # empty list is friend list | adjacency list

    # print vertices
    def printUsers(self):
        print("Total users:",len(self.users))

        keys=self.users.keys()
        for key in keys:
            print(key.getUserDetails())
        print("===========")

    # Add edge
    def connectUser(self,user1,user2):
        # connection both ways and adding edge and constructing adjacency list to a grapgh
        self.users[user1].append(user2)
        self.users[user2].append(user1)

    #     print grapgh with adjacency  list
    def printUsersWithFriendList(self):
        print("total users",len(self.users))
        keys=self.users.keys()

        for key in keys:
            print("User:",key.getUserDetails())
            friendList=self.users[key]
            for friend in friendList:
                print("Friend",friend.getUserDetails())
            print("=============")
        print("_____________________________")




def main():

        u0=User(0,"John","90909 80808","john@example.com")
        u1 = User(1, "Jennie", "96969 89895", "Jennie@example.com")
        u2 = User(2, "Sia", "95959 96969", "sia@example.com")
        u3=User(3,"Leo","92920 92920","leo@example.com")
        u4=User(4,"Fionaa","98989 96969","fionaa@example.com")
        u5 = User(5, "Kim", "91919 93939", "kim@example.com")
        u6 = User(6, "Mike", "97979 96969", "mike@example.com")

        graph=FaceBookGraph()

        graph.registeredUser(u0)
        graph.registeredUser(u1)
        graph.registeredUser(u2)
        graph.registeredUser(u3)
        graph.registeredUser(u4)
        graph.registeredUser(u5)
        graph.registeredUser(u6)

        graph.printUsers()
        graph.connectUser(u0,u1)
        graph.connectUser(u0,u2)
        graph.connectUser(u1, u2)
        graph.connectUser(u1, u3)
        graph.connectUser(u2, u4)
        graph.connectUser(u3, u4)
        graph.connectUser(u4, u5)
        graph.connectUser(u5, u6)

        graph.printUsersWithFriendList()
if __name__=='__main__':
    main()
