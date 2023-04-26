from collections import deque

H, W = map(int, input().split())

grid = [list(input()) for _ in range(H)]

black = 0

for y in range(H):
    for x in range(W):
        if grid[y][x] == "#":
            black += 1

dir = ((1, 0), (-1, 0), (0, 1), (0, -1))

dist = [[-1] * W for _ in range(H)]
dist[0][0] = 1

q = deque()
q.append([0,0])

while q:
    nowy, nowx = q.popleft()

    for dy, dx in dir:
        y = nowy + dy
        x = nowx + dx

        if 0 <= y < H  and 0 <= x < W and dist[y][x] == -1 and grid[y][x] != "#":
            dist[y][x] = dist[nowy][nowx] + 1  
            q.append([y, x])

if dist[H-1][W-1] == -1:
    print(-1)
else:
    print(H * W - dist[H-1][W-1] - black)