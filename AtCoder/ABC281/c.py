N, T = map(int, input().split())
A = list(map(int, input().split()))

T -= sum(A) * (T // sum(A))

now = 0

for i in range(N):
    if T < now + A[i]:
        print(i+1, T-now)
        break
    now += A[i]