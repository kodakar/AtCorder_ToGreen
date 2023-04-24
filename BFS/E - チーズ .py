from collections import deque

h, w, n = map(int, input().split())

c = [list(input()) for _ in range(h)]

dir = [[1,0], [0, 1], [-1, 0], [0, -1]]


def BFS(sy, sx, goal):
    dist = [[-1] * w for _ in range(h)]
    dist[sy][sx] = 0

    q = deque()
    q.append([sy, sx])

    while q:
        y, x = q.popleft()

        if c[y][x] == goal:
            break

        for dy, dx in dir:
            if 0 <= y + dy < h and 0 <= x + dx < w and c[y + dy][x + dx] != "X" and dist[y + dy][x + dx] == -1:
                dist[y + dy][x + dx] = dist[y][x] + 1
                q.append([y + dy, x + dx])
    
    return y, x, dist[y][x]

for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            sy, sx = i, j

ans = 0

for i in range(1, n+1):
    sy, sx, d = BFS(sy, sx, str(i))
    ans += d

print(ans)