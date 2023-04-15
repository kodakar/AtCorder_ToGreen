h, w, x, y = map(int, input().split())

s = [list(input()) for _ in range(h)]

x -= 1
y -= 1

ans = 0

for i in range(1,h):
    if 0 <= x - i < h:
        if s[x - i][y] == "#":
            break
        else:
            ans += 1

for i in range(1,h):
    if 0 <= x + i < h:
        if s[x + i][y] == "#":
            break
        else:
            ans += 1

for i in range(1,w):
    if 0 <= y - i < w:
        if s[x][y - i] == "#":
            break
        else:
            ans += 1

for i in range(1,w):
    if 0 <= y + i < w:
        if s[x][y + i] == "#":
            break
        else:
            ans += 1

print(ans + 1)