S = input()
T = input()

N = len(S)
M = len(T)

dp = [[None for _ in range(M+1)] for _ in range(N+1)]

dp[0][0] = 0

for i in range(N+1):
    for j in range(M+1):
        if i >= 1 and j >= 1 and S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
        elif i >= 1 and j >= 1:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i >= 1:
            dp[i][j] = dp[i-1][j]
        elif j >= 1:
            dp[i][j] = dp[i][j-1]

print(dp[N][M])
        