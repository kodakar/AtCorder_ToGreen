N, M = map(int, input().split())
a = list(map(int, input().split()))

p = []

for i in range(1, N + 1):
    p.append(i)

for i in range(M):
    x, y = a[i] - 1, a[i]
    if a[i] + 1 == a[i + 1]:
        pass
    
    p[x : y + 1] = p[y : x]

print(p)