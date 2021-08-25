# CHNGIT

for i in range(int(input())):
    n=int(input())
    list1=list(map(int,input().split()))
    list2=[]
    set1=set(list1)
    if(len(set1)==1):print(0)
    else:
        for j in set1:
            list2.append(list1.count(j))
            list2.sort()
        list2.remove(list2[-1])
        print(sum(list2))