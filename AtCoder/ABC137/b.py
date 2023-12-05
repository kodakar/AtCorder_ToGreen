K, X = map(int, input().split())

L = X - (K - 1)
R = X + (K - 1)

ans = []

for i in range(L, R+1):
    ans.append(i)

print(*ans)