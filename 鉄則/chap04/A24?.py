from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

L = [A[0]]

for i in range(1, N):
    pos = bisect_left(L, A[i])

    if len(L) <= pos:
        L.append(A[i])
    else:
        L[pos] = min(L[pos], A[i])
    
print(len(L))
