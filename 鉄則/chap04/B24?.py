from bisect import bisect_left

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

tmp = []

for x, y in XY:
    tmp.append([x, -y])

tmp.sort()

A = []
for x, y in tmp:
    A.append(-y)

LEN = 0
L = []
for i in range(N):
    pos = bisect_left(L, A[i])
    if pos == LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[pos] = A[i]

# print(L)
print(LEN)