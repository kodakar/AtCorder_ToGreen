N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i in range(1,N+1):
    if i == A[cnt]:
        print(0)
        cnt += 1
    else:
        print(A[cnt]-i)