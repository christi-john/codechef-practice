# FLOW007

def reverse(string):
    string = string[::-1]
    return string
for i in range(int(input())):
    N=str(input())
    print(int(reverse(N)))