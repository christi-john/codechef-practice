# LUCKFOUR

for i in range(int(input())):
    n=str(input())
    counter=0
    for j in n:
        if j==str(4):
            counter=counter+1
    print(counter)