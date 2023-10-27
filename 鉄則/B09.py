N = int(input())
H, W = 1500, 1500
X = [[0 for _ in range(W+1)] for _ in range(H+1)]


for i in range(N):
    A, B, C, D = map(int, input().split())
    X[A][B] += 1
    X[A][D] -= 1
    X[C][B] -= 1
    X[C][D] += 1

for i in range(H+1):
    for j in range(1, W+1):
        X[i][j] += X[i][j-1]

for i in range(1, H+1):
    for j in range(W+1):
        X[i][j] += X[i-1][j]

ans = 0

for i in range(H+1):
    for j in range(W+1):
        if X[i][j] > 0:
            ans += 1

print(ans)

