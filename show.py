#recursive fn


for i in range(0,11):
    print("  i is:", i)

def show(num):
    if num==0:
        return
    print("num is:",num)
    num=num-1
    show(num)

show(50)

# print("num is now",num)
    #execute function. can be executed again and again
# show(10)
# show(9) return is an acknowlegdement
