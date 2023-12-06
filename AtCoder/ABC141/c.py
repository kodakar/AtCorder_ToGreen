N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
P = [K] * N

for i in range(Q):
    P[A[i]-1] += 1

for i in range(N):
    if P[i] - Q <= 0:
        print("No")
    else:
        print("Yes")