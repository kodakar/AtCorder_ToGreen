from collections import deque

N, M = map(int, input().split())

connect = [[] for i in range(N + 1)]        # 都市Aからどの都市にいけるかを保持 connect[A][B]

for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)

def BFS(start):
    visited = [False] * (N + 1)             # 訪問済みを判別するための配列を用意
    visited[start] = True                   # startをTrueにする
    cnt = 1                                 # count を 1 にする
    que = deque()
    que.append(start)

    while 0 < len(que):                     # queがなくなるまで
        now_city = que.popleft()            # que の先頭をとる
        
        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                cnt += 1
                que.append(to_city)
    
    return cnt

ans = 0

for i in range(1, N + 1):
    ans += BFS(i)

print(ans)