H, W = map(int, input().split())

a = [list(map(int,input().split())) for _ in range(H)]

R = []
for i in range(H):
    R.append(sum(a[i]))

C = []
for i in range(W):
    sum = 0
    for j in range(H):
        sum += a[j][i]
    C.append(sum)

ans = []
for i in range(H):
    l = []
    for j in range(W):
        sums = R[i] + C[j] - a[i][j]
        l.append(sums)
    print(*l)