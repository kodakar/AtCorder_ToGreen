N, X = map(int, input().split())
A = list(map(int, input().split()))
new_A = []

for i in range(N):
    if A[i] != X:
        new_A.append(A[i])

print(*new_A)