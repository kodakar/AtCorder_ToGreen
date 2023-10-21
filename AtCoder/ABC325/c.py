H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

count = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                S[x][y] = "."
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == "#":
                            stack.append((nx, ny))
            count += 1

print(count)
