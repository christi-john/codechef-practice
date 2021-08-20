# ELEVSTRS

for i in range(int(input())):
    n,v1,v2=map(int,input().split())
    time=[]
    ele=2*n/v2
    st=n*(2**(1/2))/v1
    if(ele>st):print("Stairs")
    else:print("Elevator")