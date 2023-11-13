N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
r = 0
for i in range(N):
    while A[r] < A[i] + M:
        r += 1
    ans = max(ans, r-i)

print(ans)

# しゃくとり法