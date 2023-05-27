n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(m)]

dic = {}

for i in range(n):
    dic[i + 1] = set()
    dic[i + 1].add(i + 1)

for i in range(m):
    for j, k in enumerate(a[i]):
        if j + 1 < n:
            dic[k].add(a[i][j + 1])
        if j - 1 >= 0:
            dic[k].add(a[i][j - 1])

friends = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in dic[i + 1]:
        friends[i][j - 1] = True

ans = 0

for i in range(n):
    for j in range(n):
        if friends[i][j] == False:
            ans += 1
            friends[i][j] = True
            friends[j][i] = True

print(ans)