a=[0,1,2,3,4,5,6,7,8,9]
key=a[0]
m=0
c=0

print(len(a))
for i in range(0,len(a)):
    if i==m:
        c=c+1
        m=i+4
    else:pass

print("the no of counts:",c)