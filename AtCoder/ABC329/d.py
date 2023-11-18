N, M = map(int, input().split())
A = list(map(int, input().split()))

n = [0 for _ in range(N+1)]
ans = (0, 0)

for i in A:
    n[i] += 1
    ans = max(ans, (n[i],-i))
    print(-ans[1])