N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
DP = [0] * N
DP[0] = 0
DP[1] = A[1]

for i in range(2, N):
    DP[i] = min(DP[i-1] + A[i], DP[i-2] + B[i])

print(DP[-1])