N = int(input())
S = [list(input()) for _ in range(N)]

p = [[0, -1*(i+1)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if S[i][j] == "o":
            p[i][0] += 1

p.sort(reverse=True)
# print(p)

ans = []
for i in p:
    ans.append(str(-1*i[1]))

print(" ".join(ans))