# CV

for _ in range(int(input())):
    N=int(input())
    s=input()
    cont=0
    list1=['a','e','i','o','u']
    for i in range(len(s)-1):
        if s[i] not in list1 and s[i+1] in list1:
            cont+=1
    print(cont)