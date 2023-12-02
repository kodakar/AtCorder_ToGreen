N = int(input())
A = list(map(int, input().split()))

sums = [sum(A)] * N

for i in range(N):
    sums[i] -= A[i]

dic = {}

for i in range(N):
    if A[i] not in dic:
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1

a = [0] * (max(A) + 1)

for i in range(1, max(A)+1):
    a[i] = (i * dic.get(i,0) + a[i-1])

ans = []

for i in range(N):
    ans.append(sums[i] - a[A[i]] + A[i])
    
print(*ans)