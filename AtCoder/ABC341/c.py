H, W, N = map(int, input().split())
T = input()
S = [list(input()) for _ in range(H)]

def search(y, x):
    now_x = x
    now_y = y
    for i in T:
        if i == "L":
            now_x -= 1
        elif i == "R":
            now_x += 1
        elif i == "U":
            now_y -= 1
        elif i == "D":
            now_y += 1
        
        if S[now_y][now_x] == "#":
            return False
    
    return True

ans = 0

for i in range(1,H-1):
    for j in range(1,W-1):
        if S[i][j] == ".":
            if search(i, j):
                ans += 1

print(ans)