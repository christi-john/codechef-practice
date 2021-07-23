# TRICOIN

for i in range(int(input())):
    N,s=int(input()),1
    while(s*(s+1)/2<=N):s+=1
    print(s-1)