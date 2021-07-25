# RECTANGL

for i in range(int(input())):
    arr1=sorted(list(map(int,input().split())))
    if(arr1[0]==arr1[1] and arr1[2]==arr1[3]):
        print("YES")
    else: print("NO")