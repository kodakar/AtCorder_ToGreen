N, M = map(int, input().split())
P = [0 for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    P[B-1] = P[B-1] -1

cnt = 0
for i in range(N):
    if max(P) == P[i]:
        cnt += 1
    if cnt > 1:
        print(-1)
        exit()

print(P.index(max(P))+1)