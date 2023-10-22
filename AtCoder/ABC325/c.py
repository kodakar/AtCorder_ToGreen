import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
S = [[*input()] for _ in range(H)]

def DFS(i, j):
    if i < 0 or i >= H or j < 0 or j >= W or S[i][j] == '.':
        return
    
    S[i][j] = "."

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            DFS(i + dx, j + dy)

cnt = 0

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            DFS(h, w)
            cnt += 1

print(cnt)
