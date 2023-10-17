N = int(input())

g = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    x1, x2, y1, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            g[x][y] = 1

ans = 0

for i in range(100):
    ans += sum(g[i])

print(ans)