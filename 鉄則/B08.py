N = int(input())
H, W = 1500, 1500

G = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
for i in range(N):
    X, Y = map(int, input().split())
    G[X][Y] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        G[i][j] += G[i][j-1]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        G[i][j] += G[i-1][j]

Q = int(input())

for i in range(Q):
    a, b, c, d = map(int, input().split())
    print(G[c][d] - G[c][b-1] - G[a-1][d] + G[a-1][b-1])