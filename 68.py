# PERFCONT

for _ in range(int(input())):
    n,p=map(int,input().split())
    stats=list(map(int,input().split()))
    hard=0
    easy=0
    for i in stats:
        if(i>=(p/2)): easy+=1 
        elif(i<=(p/10)and i>=1):hard+=1 
    if(easy==1 and hard==2):print("yes")
    else: print("no")