# HEADBOB

for i in range(int(input())):
    ind=no=yes=0
    n=int(input())
    ges=str(input())
    for j in ges:
        if(j=="N"):no=1
        elif(j=="I"):ind=1 
        elif(j=="Y"):yes=1
    if(ind==1):print("INDIAN")
    elif(yes==1):print("NOT INDIAN")
    else:print("NOT SURE")