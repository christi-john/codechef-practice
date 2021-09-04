# AVG

for _ in range(int(input())):
    n,k,v=map(int, input().split())
    nlist=list(map(int,input().split()))
    x=(v*(n+k)-sum(nlist))/k
    if((x-int(x)==0) and x>0):print(int(x))
    else: print(-1)