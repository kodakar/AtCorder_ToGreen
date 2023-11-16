N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
dp = [0] * N

dp[0] = 0
dp[1] = A[1]

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

# print(dp)

ans = []
now = N - 1

while True:
    ans.append(now + 1)
    if now == 0:
        break

    if dp[now - 1] + A[now] == dp[now]:
        now = now - 1
    else:
        now = now - 2

print(len(ans))
print(*ans[::-1])