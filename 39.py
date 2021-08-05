# PPSUM

def summa(n):
    return (n*(n+1))/2

def summ(d,n):
    sum1=0
    for i in range(d):
        sum1=summa(n)
        n=sum1
    
    return sum1
    
if __name__=='__main__':
    for j in range(int(input())):
        d,n=map(int,input().split())
        x=(summ(d,n))
        print(int(x))