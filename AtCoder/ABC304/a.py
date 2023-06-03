n = int(input())

b = {}
c = []

for i in range(n):
    s, a = input().split()
    a = int(a)
    b[a] = s
    c.append(s)
    

index = c.index(b[min(b.keys())])

for i in (c[index:] + c[:index]):
    print(i)
