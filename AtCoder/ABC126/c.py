N, K = map(int, input().split())
ans = 0
for i in range(1,N+1):
    cnt = 0
    while True:
        if K <= i * (2 ** cnt):
            break
        cnt += 1
    ans += (1/N) * ((1/2)**cnt)
print(ans)
