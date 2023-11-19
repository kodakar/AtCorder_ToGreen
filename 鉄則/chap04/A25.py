H, W = map(int, input().split())
c = [list(input()) for i in range(H)]

dp = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    if c[i][0] == "#":
        break
    dp[i][0] = 1

for j in range(W):
    if c[0][j] == "#":
        break
    dp[0][j] = 1

for i in range(1, H):
    for j in range(1, W):
        if c[i][j] == ".":
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])