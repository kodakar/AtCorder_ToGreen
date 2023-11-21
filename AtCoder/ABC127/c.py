N, M = map(int, input().split())

max_L, min_R = -10**9, 10**9

for i in range(M):
    L, R = map(int, input().split())
    max_L = max(max_L, L)
    min_R = min(min_R, R)

if max_L <= min_R:
    print(min_R - max_L + 1)
else:
    print(0)