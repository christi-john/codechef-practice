# FLOW016

import math
for i in range(int(input())):
    list1=list(map(int,input().split()))
    a=min(list1)
    b=max(list1)
    x=int(math.gcd(a,b))
    lcm=int((a*b)/x )
    print(str(x)+" "+str(lcm))