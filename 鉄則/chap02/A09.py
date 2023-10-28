H, W, N = map(int, input().split())
snow = [[0 for _ in range(W+2)] for _ in range(H + 2)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    snow[A][B] += 1
    snow[A][D+1] -= 1
    snow[C+1][B] -= 1
    snow[C+1][D+1] += 1

for x in range(1, H + 1):
    for y in range(1, W + 1):
        snow[x][y] += snow[x][y-1]

for x in range(1, H + 1):
    for y in range(1, W + 1):
        snow[x][y] += snow[x-1][y]

for i in range(1, H+1):
    print(*snow[i][1:W+1])