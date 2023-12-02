N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

ans = 0

for i in range(N):
    for j in range(i+1,N):
        a = 0
        for k in range(D):
            a += (X[i][k] - X[j][k])**2
        if a**(1/2) == int(a**(1/2)):
            ans += 1
print(ans)