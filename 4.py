# FLOW005

for i in range(int(input())): 
    N,notes=int(input()),0
    for x in [100,50,10,5,2,1]: notes,N = notes + N//x, N%x
    print(notes)
    
# for i in range(int(input())):
#     N=int(input())
#     notes=0
#     for x in [100,50,10,5,2,1]:
#         notes = notes + N//x
#         N=N%x
#     print(notes)