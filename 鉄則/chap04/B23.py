N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

dp = [[10**9 for _ in range(N)] for _ in range(2**N)]

dp[0][0] = 0

for i in range(2**N):
    # 現在の都市 j 
    for j in range(N):
        x1, y1 = XY[j]

        if dp[i][j] < 10**9:
            # 次の都市 k
            for k in range(N):
                x2, y2 = XY[k]
                dp[i|(2**k)][k] = min(dp[i|2**k][k], dp[i][j] + ((x1-x2)**2 + (y1-y2)**2)**(1/2))
                
print(dp[-1][0])
