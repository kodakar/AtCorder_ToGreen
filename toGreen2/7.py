H, W, X, Y = map(int, input().split())

S = []
S.append(["@" for i in range(W)])
for i in range(H):
    S.append(["@"] + list(input()) + ["@"])
S.append(["@" for i in range(W)])

ans = 0

for i, j in [(1,0), (0,1), (-1,0),(0,-1)]:
    for k in range(1,max(H, W)):
        if S[X + k * i][Y + k * j] == ".":
            ans += 1
        else:
            break

print(ans + 1)