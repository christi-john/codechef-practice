# HARDBET

for i in range(int(input())):
    Sa,Sb,Sc=map(int,input().split())
    if(Sa<Sb and Sa<Sc):print("Draw")
    elif(Sb<Sa and Sb<Sc): print("Bob")
    elif(Sc<Sa and Sc<Sb): print("Alice")