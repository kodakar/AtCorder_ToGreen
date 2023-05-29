N, M = map(int, input().split())

S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0

for i in S:
    for j in T:
        if i[-3:] == j:
            ans += 1
            break

print(ans)