N = int(input())
A = [0] + list(map(int, input().split()))
D = int(input())

P, Q = [], []

for i in A:
    P.append(i)
    Q.append(i)

for i in range(1, N+1):
    P[i] = max(P[i], P[i-1])

for i in range(N-1, -1, -1):
    Q[i] = max(Q[i], Q[i+1])

for i in range(D):
    L, R = map(int, input().split())
    print(max(P[L-1], Q[R+1]))