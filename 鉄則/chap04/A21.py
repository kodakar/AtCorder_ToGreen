N = int(input())

PA = [list(map(int, input().split())) for _ in range(N)]

dp = [[None for _ in range(N+1)] for _ in range(N+1)]
dp[1][N] = 0

for LEN in reversed(range(0, N-1)):
    for l in range(1, N-LEN+1):
        r = l + LEN

        score1 = 0
        if l >= 2 and l <= PA[l-2][0] and PA[l-2][0] <= r:
            score1 = PA[l-2][1]

        score2 = 0
        if r <= N - 1 and l <= PA[r][0] and PA[r][0] <= r:
            score2 = PA[r][1]
        
        if l == 1:
            dp[l][r] = dp[l][r+1] + score2
        elif r == N:
            dp[l][r] = dp[l-1][r] + score1
        else:
            dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)

ans = 0
for i in range(1, N+1):
    ans = max(ans, dp[i][i])
print(ans)