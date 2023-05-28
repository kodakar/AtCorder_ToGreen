from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
tmp = deque()

for i in range(1, N + 1):
    if i not in A:
        tmp.appendleft(i)
        ans += list(tmp)
        tmp.clear()
    else:
        tmp.appendleft(i)

print(*ans)