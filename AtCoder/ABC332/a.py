N, S, K = map(int, input().split())
PQ = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    ans += PQ[i][0] * PQ[i][1]

if ans >= S:
    print(ans)
else:
    print(ans+K)