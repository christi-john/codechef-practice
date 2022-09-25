#Simple Statisics 

# cook your dish here
for i in range(int(input())):
    N,K=list(map(int, input().split()))
    numbers=list(map(int,input().split()))
    numbers.sort()
    print('%.6f'% float((sum(numbers[K:N-K]))/len(numbers[K:N-K])))