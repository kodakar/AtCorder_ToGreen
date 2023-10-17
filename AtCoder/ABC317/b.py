N = int(input())
A = list(map(int, input().split()))

A.sort()

for i in range(N-1):
    if A[i+1] - A[i] == 2:
        print(A[i] + 1)
        exit()

