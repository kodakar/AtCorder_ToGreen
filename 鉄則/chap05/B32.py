N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [None] * (N + 1)

for i in range(N+1):
    dp[i] = False
    for j in range(K):
        if i >= A[j] and dp[i-A[j]] == False:
            dp[i] = True

print("First" if dp[N] else "Second")