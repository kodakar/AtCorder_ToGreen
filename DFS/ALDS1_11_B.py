n = int(input())

nodes = []

for _ in range(n):
    a = list(map(int, input().split()))
    u, k = a[:2]
    v = a[2:]
    v.sort()
    nodes.append(v)

d = [-1 for _ in range(n)]
f = [-1 for _ in range(n)]

global count

count = 1

def DFS(start):
    global count

    if d[start] != -1:
        return
    
    d[start] = count
    count += 1

    for i in nodes[start]:
        DFS(i - 1)
    
    f[start] = count
    count += 1

for i in range(n):
    DFS(i)

    print(i + 1, d[i], f[i])

print(d,"/",f)
print(nodes)
print(count)