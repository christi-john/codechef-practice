# JDELAY

for i in range(int(input())):
    n=int(input())
    list1=[]
    count=0
    for j in range(n):
        times=list(map(int,input().split()))
        c=max(times)-min(times)
        list1.append(c)
    for x in list1:
        if(x>5):
            count+=1 
    print(count)