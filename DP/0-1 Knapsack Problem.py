N, W = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]

DP = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j < a[i][1]:
            DP[i + 1][j] = DP[i][j]
        else:
            DP[i + 1][j] = max(DP[i][j], DP[i][j - a[i][1]] + a[i][0])

print(DP[N][W])