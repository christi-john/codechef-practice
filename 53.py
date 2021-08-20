# MSNSADM1

for i in range(int(input())):
    n=int(input())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    list3=[]
    list4=[]
    list5=[]
    for j in list1:list3.append(20*j)
    for k in list2:list4.append(10*k)
    for a in range(len(list3)):
        list5.append(list3[a]-list4[a])
    maxi=max(list5)
    if(maxi>0):print(maxi)
    else:print(0)