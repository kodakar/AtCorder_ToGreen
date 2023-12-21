A, B, C, K = map(int, input().split())
ans = 0
if K <= A + B:
    if A < K:
        ans += A
    else:
        ans += K
else:
    ans += A - (K - (A + B))

print(ans)