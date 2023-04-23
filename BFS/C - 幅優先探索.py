from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

c = [list(input()) for _ in range(R)]

q = deque()

q.appendleft([sy, sx])

dist = [[-1] * C for i in range(R)]
dist[sy][sx] = 0

while q:
    nowy, nowx = q.popleft()

    for dy, dx in [[1,0], [0,1], [-1,0], [0,-1]]:
        toy = nowy + dy
        tox = nowx + dx
        
        if (toy <= 0 or toy >= R) or (tox <= 0 or tox >= C):
            continue

        if c[toy][tox] == "#":
            continue

        if dist[toy][tox] == -1:
            q.append([toy, tox])
            dist[toy][tox] = dist[nowy][nowx] + 1

    
print(dist[gy][gx])