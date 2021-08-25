# MISSP

for i in range(int(input())):
    list1=[]
    for j in range(int(input())):
        list1.append(int(input()))
    for k in list1:
        if(list1.count(k)%2!=0): 
            print(k)
            break