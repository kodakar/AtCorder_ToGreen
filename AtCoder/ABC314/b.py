N = int(input())

a = []

for i in range(N):
    C = int(input())
    A = list(map(int,input().split()))
    a.append(A)

X = int(input())

b = {}

for i in range(N):
    if X in a[i]:
        if len(a[i]) not in b:
            b[len(a[i])] = [i+1]
        else:
            b[len(a[i])].append(i+1)

if not b:
    print(0)
    print()
    exit()

if b[min(b)]:
    print(len(b[min(b)]))
    print(*b[min(b)])