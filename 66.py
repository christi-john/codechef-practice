# PSGRADE

for _ in range(int(input())):
    amin,bmin,cmin,tmin,a,b,c=map(int,input().split())
    summ=a+b+c
    if((summ>=tmin) and (a>=amin) and (b>=bmin) and (c>=cmin)):print("YES")
    else: print("NO")