N, X = map(int, input().split())
A = 0

for i in range(N):
    V, P = map(int, input().split())
    A += V * P

    if X * 100 < A:
        print(i+1)
        exit()

print(-1)