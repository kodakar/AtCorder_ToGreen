H, W = (8, 8)

S = [list(input()) for i in range(H)]

a = ["a", "b", "c", "d", "e", "f", "g", "h"]
b = ["8", "7", "6", "5", "4", "3", "2", "1"]

pos = [[ i + j for i in a] for j in b]

for i in range(H):
    for j in range(W):
        if S[i][j] == "*":
            print(pos[i][j])