N = int(input())

A = list(map(int, input().split()))
A.sort()

Q = int(input())

for i in range(Q):
    X = int(input())
    L = 0
    R = len(A) - 1
    mid = len(A)//2
    while True:
        if X <= A[mid]:
            R = mid - 1
        elif A[mid] < X:
            L = mid + 1
        mid = (R + L)//2
        if R < L:
            print(mid+1)
            break