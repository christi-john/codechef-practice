# HS08TEST

amt,bal=map(float,input().split())
if(int(amt)%5==0):
    if(amt<=(bal-0.5)): print("{:.2f}".format(bal-0.5-amt))
    else: print("{:.2f}".format(bal))
else: print("{:.2f}".format(bal))