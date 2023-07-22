N, D = map(int, input().split())
S = [input() for _ in range(N)]

a = list(S[0])

for i in range(N):
    for j in range(D):
        if S[i][j] == "x":
            a[j] = "x"

cnt = 0
ans = []

for i in range(len(a)):
    if a[i] == "o":
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

ans.append(cnt)

print(max(ans))