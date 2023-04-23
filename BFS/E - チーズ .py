from collections import deque

h, w, n = map(int, input().split())

c = [list(input()) for _ in range(h)]

fac = []

for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            sy, sx = i, j
        if c[i][j] != "S" and c[i][j] !="." and c[i][j] != "X" :
            fac.append(c[i][j]) 

dist = [[-1] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]



dist[sy][sx] = 0
visited[sy][sx] = True

q = deque()
q.append([sy, sx])

count = 0

while q:
    now_y, now_x = q.popleft()

    for dy, dx in [[1,0], [0, 1], [-1, 0], [0, -1]]:
        next_y = now_y + dy
        next_x = now_x + dx

        if (next_y < 0 or h - 1 < next_y) or (next_x < 0 or w - 1 < next_x):
            continue

        if c[next_y][next_x] == "X":
            continue
        
        if visited[next_y][next_x] == False:
            visited[next_y][next_x] = True
            q.append([next_y, next_x])
            dist[next_y][next_x] = dist[now_y][now_x] + 1

        if c[next_y][next_x] != "." and c[next_y][next_x] != "X" and c[next_y][next_x] != "S":
            if int(c[next_y][next_x]) <= n:
                q = deque()
                q.append([next_y, next_x])
                n += int(c[next_y][next_x])
                visited = [[False] * w for _ in range(h)]
                visited[next_y][next_x] = True
                count += 1
                c[next_y][next_x] = "."
                print(dist)
                print(q)
                break

        print(dist)
        print(q)

        if len(fac) == count:
            print(dist[next_y][next_x])
            exit()