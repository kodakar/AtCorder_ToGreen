N, M = map(int, input().split())
S = [[*input()] for i in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        a = set()
        for k in range(M):
            if S[i][k] == "o" or S[j][k] == "o":
                a.add(k)
        if len(a) == M:
            ans += 1
print(ans)
