# LCH15JAB

for i in range(int(input())):
    s=list(input())
    list1=[]
    for j in set(s):
        list1.append(s.count(j))
        list1.sort()
    vari=list1[-1]
    list1.remove(list1[-1])
    if(sum(list1)==vari): print("YES")
    else: print("NO")