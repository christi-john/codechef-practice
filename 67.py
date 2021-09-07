# CNDLOVE

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    tot=sum(a)
    if(tot%2!=0):print("YES")
    else: print("NO")