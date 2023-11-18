import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

print(A[bisect.bisect_left(A, max(A))-1])