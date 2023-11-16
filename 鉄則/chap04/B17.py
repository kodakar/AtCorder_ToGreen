N = int(input())
h = list(map(int, input().split()))

dp = [None] * N

dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

# print(dp)

ans = []
now = N - 1

while True:
    ans.append(now + 1)

    if now == 0:
        break

    if dp[now-1] + abs(h[now] - h[now-1]) == dp[now]:
        now = now - 1
    else:
        now = now - 2

print(len(ans))
print(*ans[::-1])