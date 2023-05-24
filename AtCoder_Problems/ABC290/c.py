N, K = map(int, input().split())
A = list(map(int, input().split()))

if 0 not in A:
    print(0)
    exit()

n = [0 for _ in range(K)]

for i in A:
    if i < K:
        n[i] += 1

if 0 in n:
    print(n.index(0))   
else:
    print(K)