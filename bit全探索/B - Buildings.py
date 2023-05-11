from itertools import combinations

N, K = map(int, input().split())

a = list(map(int, input().split()))

ans = 10 ** 18
    
for builds in combinations(range(1, N), K - 1):
    mx = a[0]
    t_ans = 0
    for i in range(1, N):
        if i in builds:
            if mx >= a[i]:
                mx += 1
                t_ans += mx - a[i]
            else:
                mx = a[i]
        else:
            mx = max(mx, a[i])
    
    ans = min(ans, t_ans)

print(ans)