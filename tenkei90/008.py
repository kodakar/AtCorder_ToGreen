# 2^N の全探索は DP で解けることが多い
T = "atcoder"
MOD = 10**9 + 7

def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a

N = int(input())
S = input()


dp = [[0]*(len(T)+1) for _ in range(N+1)]

dp[0][0] = 1

for i in range(N):
    for j in range(len(T)+1):
        dp[i+1][j] = add(dp[i+1][j], dp[i][j])

        if (j < len(T)) and S[i] == T[j]:
            dp[i+1][j+1] = add(dp[i+1][j+1], dp[i][j])

print(" ", 0, "a","t","c","o","d","e","r")
for i in range(N+1):
    if i == 0:
        print(0, *dp[i])
    else:
        print(S[i-1] ,*dp[i])
print(dp[N][len(T)])