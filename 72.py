# COMM3

import math
for _ in range(int(input())):
    r=int(input())
    chefx,chefy=map(int,input().split())
    headx,heady=map(int,input().split())
    sousx,sousy=map(int,input().split())
    dist1=math.sqrt(((headx-chefx)**2)+((heady-chefy)**2))
    dist2=math.sqrt(((headx-sousx)**2)+((heady-sousy)**2))
    dist3=math.sqrt(((sousx-chefx)**2)+((sousy-chefy)**2))
    if((dist1<=r and dist2<=r)or(dist3<=r and dist2<=r) or (dist1<=r and dist3<=r)):
        print("yes")
    else: print("no")