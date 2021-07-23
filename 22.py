#  FLOW009

for i in range(int(input())):
    quantity,price=map(float,input().split(" "))
    amt=quantity*price
    if quantity>1000: print("{:.6f}".format(0.9*amt))
    else: print("{:.6f}".format(amt))