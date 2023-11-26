N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0

for i in range(2**N):
    s_on = [0] * M
    for shift in range(N):
        if i >> shift & 1 == 1:
            for j in range(M):
                if shift + 1 in ks[j][1:]:
                    s_on[j] += 1
    
    l_on = 0

    for k in range(M):
        if s_on[k] % 2 == p[k]:
            l_on += 1
    
    if l_on == M:
        ans += 1

print(ans)

