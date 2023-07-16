N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    p = a[i][0]
    c = a[i][1]
    f = a[i][2:]
    for j in range(N):
        p2 = a[j][0]
        c2 = a[j][1]
        f2 = a[j][2:]

        if p >= p2:
            count = 0
            for k in f:
                if k in f2:
                    count += 1
            if count >= c:
                if p > p2 or c2 > c:
                    print("Yes")
                    exit()

print("No")
