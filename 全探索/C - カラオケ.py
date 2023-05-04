n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

score = []

for j in range(m):
    for k in range(j, m):
        b = 0
        for i in range(n):
            b += max(a[i][j], a[i][k])
        
        score.append(b)

print(max(score))