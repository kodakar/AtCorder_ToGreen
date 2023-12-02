N, S, M, L = map(int, input().split())

ans = 10**10

for s in range(18):
    for m in range(14):
        for l in range(10):
            if N <= (s * 6) + (m * 8) + (l * 12):
                ans = min(ans, (s * S) + (m * M) + (l * L))

print(ans)