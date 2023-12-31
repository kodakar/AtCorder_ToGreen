H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

min_A = float("inf")

for i in range(H):
    min_A = min(min_A, min(A[i]))

ans = 0

for i in range(H):
    for j in range(W):
        ans += A[i][j] - min_A

print(ans)