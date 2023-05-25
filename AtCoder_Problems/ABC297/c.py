H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if 0 <= y < H and 0 <= x < W - 1:
            if S[y][x] == "T" and S[y][x + 1] == "T":
                S[y][x], S[y][x + 1] = ("P", "C")

for i in range(H):
    print("".join(S[i]))