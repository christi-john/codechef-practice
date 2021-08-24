# CHN15A

for i in range(int(input())):
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    counter=0
    list2=[]
    for j in list1:
        list2.append(j+k)
    for x in list2:
        if(x%7==0):counter+=1
    print(counter)