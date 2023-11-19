N, M = map(int, input().split())

A = []
for i in range(M):
    a = list(map(int, input().split()))
    n = 0
    for j in range(len(a)):
        if a[j] == 1:
            n += 2**j
    A.append(n)

dp = [[10**9 for _ in range(2**N)] for _ in range(M+1)]
dp[0][0] = 0

for i in range(1, M+1):
    for j in range(2**N):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][j|A[i-1]] = min(dp[i][j|A[i-1]], dp[i-1][j]+1)


print(dp[M][-1] if dp[M][-1] != 10**9 else -1)