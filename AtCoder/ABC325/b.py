N = int(input())

W = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(24):
    p = 0
    for j in W:
        time = (i + j[1]) % 24
        if 9 <= time <= 17:
            p += j[0]
    ans = max(ans, p)

print(ans)




