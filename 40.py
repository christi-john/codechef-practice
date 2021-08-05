# PRB01

for i in range(int(input())):
    num=int(input())
    prime=0
    if(num==0 or num==1): print("no")
    else:
        for j in range(2,num):
            if(num%j==0): prime=1
        if(prime==1):print("no")
        else: print("yes")