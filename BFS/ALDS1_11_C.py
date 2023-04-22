from collections import deque

class Info:
    def __init__(self,arg_node_id,arg_sum_cost):
        self.node_id = arg_node_id
        self.sum_cost = arg_sum_cost

n = int(input())

connect = [[] for i in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    id = a[0] - 1
    for j in range(a[1]):
        connect[id].append(a[2 + j] - 1)

visited = [False] * n
visited[0] = True

min_dist = [-1] * n
min_dist[0] = 0

q = deque()
q.append((Info(0,0)))

while len(q) > 0:
    info = q.popleft()

    for next in connect[info.node_id]:
        if visited[next] == True:
            continue

        visited[next] = True
        min_dist[next] = info.sum_cost + 1
        q.append(Info(next, min_dist[next]))

for i in range(n):
    print("%d %d"%(i+1,min_dist[i]))