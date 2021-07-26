# AMR15A

N=int(input())
counter1=0
counter2=0
arr=list(map(int,input().split()))
for j in range(N):
    if arr[j]%2==0: counter1+=1
    else: counter2+=1
if counter1>counter2: print("READY FOR BATTLE")
else: print("NOT READY")