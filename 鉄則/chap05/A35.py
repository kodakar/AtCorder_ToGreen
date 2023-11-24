N = int(input())
A = list(map(int, input().split()))

dp = [[None for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    dp[N][i] = A[i-1]

for i in range(N-1, -1, -1):
    for j in range(1, i+1):
        if i % 2 == 0:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

print(dp[1][1])