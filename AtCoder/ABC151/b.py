N, K, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K+1):
    if (sum(A) + i) / N >= M:
        print(i)
        exit()
print(-1)