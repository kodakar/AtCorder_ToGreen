import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in itertools.permutations(range(1,N)):
    now = 0
    time = 0
    
    for j in i:
        time += T[now][j]
        now = j

    time += T[now][0]

    if time == K:
        ans += 1

print(ans)