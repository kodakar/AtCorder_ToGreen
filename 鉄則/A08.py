H, W = map(int, input().split())

X = [([0]+list(map(int, input().split())) + [0]) for _ in range(H)]
X = [[0 for _ in range(W+2)]] + X
X += [[0 for _ in range(W+2)]]

Q = int(input())


for i in range(1, H+1):
    for j in range(1, W+1):
        X[i][j] += X[i][j-1]
        
for i in range(1, H+1):
    for j in range(1, W+1):
        X[i][j] += X[i-1][j]

for i in range(Q):
    A, B, C, D = map(int, input().split())
    print(X[C][D] - X[C][B-1] - X[A-1][D] + X[A-1][B-1])
