R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

for r in range(R):
    for c in range(C):
        if B[r][c] != "." and B[r][c] != "#":
            for r2 in range(R):
                for c2 in range(C):
                    if abs(r - r2) + abs(c - c2) <= int(B[r][c]) and (B[r2][c2] == "." or B[r2][c2] == "#"):
                        B[r2][c2] = "."
            B[r][c] = "."
            
for i in range(R):
    print("".join(B[i]))

