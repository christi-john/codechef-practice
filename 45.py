# MATCHES

for i in range(int(input())):
    a,b=map(int,input().split())
    addn=str(a+b)
    ans=0
    for j in addn:
        if(j=="0" or j=="6" or j=="9"):ans=ans+6
        elif(j=="1"):ans=ans+2
        elif(j=="5" or j=="2" or j=="3"):ans=ans+5
        elif(j=="4"):ans=ans+4 
        elif(j=="7"):ans=ans+3 
        elif(j=="8"):ans=ans+7 
    print(ans)