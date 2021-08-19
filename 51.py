# TABLET

for i in range(int(input())):
    N,B=map(int,input().split())
    list1=[]
    for j in range(N):
        W,H,P=map(int,input().split())
        area=W*H
        if(P<=B):list1.append(area)
    if(list1==[]):print("no tablet")
    else:print(max(list1))