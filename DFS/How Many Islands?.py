def DFS(now):
        global count

        nowy, nowx = now

        if visited[nowy][nowx] == False:
            visited[nowy][nowx] = True
            count += 1

        for dy, dx in dir:
            y = nowy + dy
            x = nowx + dx

            if 0 <= y < h and 0 <= x < w and visited[y][x] != False:
                continue
            
            if 0 <= y < h and 0 <= x < w and visited[y][x] == False and c[y][x] == 1:
                visited[y][x] = True
                DFS((y, x))
                
while True:

    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    c = [list(map(int, input().split())) for _ in range(h)]

    dir = ((1,0), (-1,0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1))

    visited = [[False for _ in range(w)] for _ in range(h)]

    count = 0

    for y in range(h):
        for x in range(w):
            if c[y][x] == 1:
                DFS([y, x])

    print(count)

