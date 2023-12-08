N = int(input())
A = list(map(int, input().split()))

tmp = []

for i, n in enumerate(A):
    tmp.append([n,i+1])

ans = []

for i in sorted(tmp):
    ans.append(i[1])

print(*ans)