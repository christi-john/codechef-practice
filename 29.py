# CRICRANK

for i in range(int(input())):
    AR,AW,AC=map(int,input().split())
    BR,BW,BC=map(int,input().split())
    if AR>BR and AW>BW and AC>BC: print("A")
    elif AR>BR and AW>BW: print("A")
    elif AR>BR and AC>BC: print("A")
    elif AC>BC and AW>BW: print("A")
    else: print("B")