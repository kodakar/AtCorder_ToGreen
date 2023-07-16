from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())


A = sorted(A)
ok = 0
ng = N

for _ in range(Q):
    B = int(input())
    j = bisect_left(A, B)
    # print(A,j)

    res = 10**9
    if j < N:
        res = min(res, abs(A[j] - B))
    if j > 0:
        res = min(res, abs(A[j-1]-B))
    
    print(res)