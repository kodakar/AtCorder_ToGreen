from bisect import bisect_left 

N = int(input())
A = list(map(int, input().split()))
tmp = []
for i in set(A):
    tmp.append(i)
    
tmp.sort()

B = []
for i in A:
    pos = bisect_left(tmp, i)
    B.append(pos+1)

print(*B)