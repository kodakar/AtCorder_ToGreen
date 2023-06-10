H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

for Y in range(H):
    for X in range(W):
        if s[Y][X] == "#":
            if Y + 1 < H and 0 <= X - 1:
                if s[Y + 1][X - 1] == "#":
                    print(Y + 1, X)
                    exit()
            
            for y in range(Y, H):
                for x in range(X, W):
                    if s[y][x] == ".":
                        if y == H - 1 or s[y + 1][x] != ".":
                            print(y+1, x+1)
                            exit()
            

