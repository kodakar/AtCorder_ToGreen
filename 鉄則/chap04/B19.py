N, W = map(int, input().split())

dp = [[10**15 for _ in range(100001)] for _ in range(N+1)]

dp[0][0] = 0

for i in range(1, N+1):
    w, v = list(map(int, input().split()))
    for j in range(100001):
        if j < v:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v] + w)

ans = 0
for i in range(100001):
    if dp[N][i] <= W:
        ans = i

print(ans)