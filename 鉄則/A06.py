N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A

for i in range(1, N):
    A[i] += A[i-1]

for i in range(Q):
    L, R = map(int, input().split())
    print(A[R] - A[L-1])