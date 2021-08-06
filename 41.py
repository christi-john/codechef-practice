# LOSTMAX

list1=[]
for i in range(int(input())):
    list1=list(map(int,input().split()))
    list1.remove(len(list1)-1)
    print(max(list1))