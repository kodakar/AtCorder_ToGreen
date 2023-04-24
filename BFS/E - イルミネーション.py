from collections import deque

W, H = map(int, input().split())

# b = [list(map(int, input().split())) for _ in range(H)]

oddD = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1]]
evenD = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1]]

b = []
b.append([0] * (W + 2))
for i in range(H):
    a = list(map(int, input().split()))
    a = [0] +  a + [0]
    b.append(a)
b.append([0] * (W + 2))

visited = [[False] * (W + 2) for _ in range(H + 2)]
visited[0][0] = True

q = deque()
q.append([0, 0])

count = 0

while q:
    y, x = q.popleft()

    if y % 2 == 0:
        dydx = evenD
    else:
        dydx = oddD
    
    for dy, dx in dydx:
        if (0 <= y + dy < H + 2) and (0 <= x + dx < W + 2) and visited[y + dy][x + dx] == False:
            if b[y + dy][x + dx] == 1:
                count += 1
                continue

            visited[y + dy][x + dx] = True
            q.append([y + dy, x + dx])
    

print(count)