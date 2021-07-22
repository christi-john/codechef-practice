# REMISS

for i in range(int(input())):
    A,B = map(int,input().split())
    if A>B: print(str(A) + " " + str(A+B))
    else: print(str(B) + " " + str(A+B))