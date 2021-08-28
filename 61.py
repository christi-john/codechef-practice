# BIT2A

for i in range(int(input())):
    n=int(input())
    list1=list(map(int,input().split()))
    list2=[]
    #ans=""
    for j in list1:
        counter=0
        for k in list1:
            if(j<k):
                counter+=1
        #list2.append(counter)
        print(counter,end=" ")
    print()
    #print(*list2)
    # for _ in list2:
    #     ans=ans+str(_)+" "
    # print(ans)