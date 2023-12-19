N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
a = sum(A)
for i in range(N):
    if A[i] < a/(4*M):
        A[i] = -10**10
print("Yes" if 0 <= sum(A[:M]) else "No")