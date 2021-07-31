# ATM2

for i in range(int(input())):
    temp=0
    stringg=""
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for j in a:
        temp=temp+j 
        if(temp<=k):
            print(stringg+"1",end="")
        else:
            print(stringg+"0",end="")
            temp=temp-j
    print()