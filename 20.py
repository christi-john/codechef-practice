# PALL01

for i in range(int(input())):
    N=str(input())
    N1=N [::-1]   #reversing string
    if N1==N: print("wins")
    else: print("loses")