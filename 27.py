# GDOG

for i in range(int(input())):
    list1=[]
    N,K=map(int, input().split())
    for j in range(1,K+1):
        list1.append(N%j)
    print(max(list1))