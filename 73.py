# AVG

for i in range(int(input())):
    n,k,v=list(map(int, input().split()))
    list1=list(map(int,input().split()))
    n1=(v*(n+k)) - sum(list1)
    if(n1%k==0 and n1/k>0):print(int(n1/k))
    else: print(-1)