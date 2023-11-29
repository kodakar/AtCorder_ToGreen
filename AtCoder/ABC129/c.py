N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]

ng = [False] * (N + 1)
for i in A:
    ng[i] = True

dp = [0] * (N + 1)

dp[0] = 1
for i in range(N):
    if ng[i+1] == False:
        dp[i+1] += dp[i]

    if i + 2 <= N and ng[i+2] == False:
        dp[i+2] += dp[i]

print(dp[N]%1000000007)