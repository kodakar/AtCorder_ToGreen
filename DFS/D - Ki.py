N, Q = map(int, input().split())

nodes = [[] for _ in range(N)]
counter = [[] for _ in range(N)]

point = [0 for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    nodes[a - 1].append(b-1)

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p - 1].append(x)

visited = [False for _ in range(N)]
visited[0] = True

point[0] = sum(counter[0])

def dfs(now):
    for i in nodes[now]:
        if visited[i] == False:
            point[i] = point[now] + sum(counter[i])
            visited[i] = True
            dfs(i)

dfs(0)

print(*point)