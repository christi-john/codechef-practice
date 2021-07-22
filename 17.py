# CHOPRT

for i in range(int(input())):
    A,B=map(int,input().split())
    if A<B: print("<")
    elif A>B: print(">")
    elif A==B: print("=")