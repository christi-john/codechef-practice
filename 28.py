# THREDICE

for i in range(int(input())):
    counter=0
    X,Y=map(int,input().split())
    summ=X+Y
    for j in range(summ+1,7):
        counter+=1
    print(counter/6)