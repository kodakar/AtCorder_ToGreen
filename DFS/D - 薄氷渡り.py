m = int(input())    # row
n = int(input())    # column

ice = [list(map(int, input().split())) for _ in range(n)]       # ice

dir = ((1,0), (0,1), (-1, 0), (0, -1))      # direction

def DFS(nowy, nowx):
    dist = 0

    for dy, dx in dir:
        y = nowy + dy
        x = nowx + dx

        if 0 <= y < n and 0 <= x < m and ice[y][x] == 1:
            ice[y][x] = 0
            dist = max(dist, DFS(y, x))
            ice[y][x] = 1
    
    return dist + 1

ans = 0

for y in range(n):
    for x in range(m):
        if ice[y][x] == 1:
            ice[y][x] = 0
            ans = max(ans, DFS(y, x))
            ice[y][x] = 1

print(ans)