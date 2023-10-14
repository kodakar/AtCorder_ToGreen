N, X = map(int, input().split())
A = list(map(int,input().split()))

A.sort()

nokori = X - sum(A[1:N-2])

if nokori <= A[0]:
    print(0)
elif nokori > A[-1]:
    print(-1)
elif A[0] < nokori <= A[-1]:
    print(nokori)