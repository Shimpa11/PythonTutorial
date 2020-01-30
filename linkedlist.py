"""
1.Think of an object
song:title,artist,duration
"""
# 2. create its class

class Song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist = artist
        self.duration=duration
        nextSong=None
        previousSong=None


    def showSong(self):
        print("!!!{}!!! {}!!!{}!!!".format(self.title,self.artist,self.duration))



# from the class create real objects
song1=Song("Duniyaa",         "Akhil", 2.56)
song2=Song("Pachtaoge" ,      "Arijit Singh", 2.56)
song3=Song("Tera Ban Jaunga" ,"Kabir Singh", "2:56")
song4=Song("Vaaste" ,         "Dhvani", "2:56")
song5=Song("Tum Hi Aana" ,    "Payal Dev ","2:56")

# print("song1 is:",song1)
# print("song2 is:",song2)
# print("song3 is:",song3)
# print("song4 is:",song4)
# print("song5 is:",song5)

songs=[song1,song2,song3,song4,song5]
for song in songs:
    print(song)

# reference copy operation
song1.nextSong=song2
song2.nextSong=song3
song3.nextSong=song4
song4.nextSong=song5
song5.nextSong=song1


song1.previousSong=song5
song2.previousSong=song1
song3.previousSong=song2
song4.previousSong=song3
song5.previousSong=song4

# song1.showSong()
# song1.nextSong.showSong()
# song1.previousSong.showSong()

print("Iterating Forward")
temp=song1
while temp.nextSong!=song1:
    print("------------")
    temp.showSong()
    temp=temp.nextSong
print("--------------------")
# showing the last song
temp.showSong()
print("-----------------------")



print("Iterating backward")

current=song5
while current.previousSong!=song5:
    print("-------------")
    current.showSong()
    current=current.previousSong
print("--------------")
current.showSong()
print("--------------")