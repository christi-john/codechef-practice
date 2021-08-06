# SMPAIR

for i in range(int(input())):
    n=int(input())
    list1=list(map(int,input().split()))
    n1=min(list1)
    list1.remove(n1)
    n2=min(list1)
    print(n1+n2)