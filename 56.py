# CCOOK

for i in range(int(input())):
    list1=list(map(int,input().split()))
    addd=0
    for j in list1:
        addd=addd+j
    if(addd==0):print("Beginner")
    elif(addd==1):print("Junior Developer")
    elif(addd==2):print("Middle Developer")
    elif(addd==3):print("Senior Developer")
    elif(addd==4):print("Hacker")
    else: print("Jeff Dean")