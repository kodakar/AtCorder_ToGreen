from collections import deque

while True:

    w, h = map(int, input().split())

    if w == 0 and h == 0:
        exit()
        
    c = [list(map(int, input().split())) for _ in range(2 * h - 1)]

    yokokabe = c[::2]
    tatekabe = c[1::2]

    dir = [[1, 0],[-1, 0],[0, 1],[0, -1]]

    dist = [[-1] * w for _ in range(h)]
    dist[0][0] = 1
    dist[h - 1][w - 1] = 0

    wall = [[[False, False, False, False] for _ in range(w)] for _ in range(h)] # up down right left


    for y in range(h):
        for x in range(w - 1):
            if yokokabe[y][x] == 1:
                wall[y][x][2] = True
                wall[y][x + 1][3] = True


    for y in range(h - 1):
        for x in range(w):
            if tatekabe[y][x] == 1:
                wall[y][x][1] = True
                wall[y + 1][x][0] = True

    q = deque()
    q.append([0, 0])

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in dir:
            y = nowy + dy
            x = nowx + dx

            if (0 <= y < h) and (0 <= x < w):
                
                if dy == -1 and wall[nowy][nowx][0] == True:      # up
                    continue

                if dy == 1 and wall[nowy][nowx][1] == True:       # down
                    continue

                if dx == 1 and wall[nowy][nowx][2] == True:       # right
                    continue

                if dx == -1 and wall[nowy][nowx][3] == True:      # left
                    continue

                if dist[y][x] == -1:
                    dist[y][x] = dist[nowy][nowx] + 1
                    q.append([y, x])

                elif y == h - 1 and x == w - 1:
                    dist[y][x] = dist[nowy][nowx] + 1
                    break

    print(dist[h-1][w-1])
