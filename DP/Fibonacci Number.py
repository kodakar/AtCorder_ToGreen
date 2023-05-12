n = int(input())

def fib(n):
    DP =[0 for _ in range(n + 1)]
    DP[0] = 1
    DP[1] = 1

    for i in range(2, n + 1):
        DP[i] = DP[i - 2] + DP[i - 1]
    
    return DP[n]


print(fib(n))
