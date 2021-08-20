# PLAYPIAN

for i in range(int(input())):
    s=input()
    
    # ok=1
    # for i in range(0,len(s)-1,2):
    #     if(s[i]==s[i+1]):
    #         ok=0
    # if(ok==0):print("no")
    # else:print("yes")
    
    for i in range(0,len(s)-1,2):
        if(s[i]==s[i+1]):
            print("no")
            break
    else:print("yes")