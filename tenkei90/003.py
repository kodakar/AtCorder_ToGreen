# 最短経路問題

N = int(input())
G = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    dist = [-1 for _ in range(N+1)]
    dist[s] = 0
    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
    return dist

dist1 = dfs(1)                  # dfsで1から一番離れたところを求める
index = dist1.index(max(dist1))
ans = dfs(index)                # そこから一番遠いところ +1 が答え
print(max(ans) + 1)