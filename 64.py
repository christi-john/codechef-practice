# MDL

for _ in range(int(input())):
    n=int(input())
    list1=[]
    a=list(map(int,input().split()))
    for i in a:
        if(i==min(a)or i==max(a)):
            list1.append(i)
    print(*list1)