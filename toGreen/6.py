n = int(input())

m = []

for i in range(n):
    s, t = map(str, input().split())
    m.append([t, s])

m.sort(reverse=True)

print(m[1][1])