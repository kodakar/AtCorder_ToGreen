N = int(input())

# 表を作成

h = [0] + list(map(int, input().split())) # [0] を最初に入れる理由は わかりやすくするため。　問題によって適宜変える
dp = [10 ** 15] * (N + 1) # 最小値なのでバカでかい数入れておく


# 表のすぐわかるところを埋めておく

dp[1] = 0
dp[2] = abs(h[2] - h[1])


# 表を埋めていく

for i in range(3, N + 1):
    cost2 = dp[i-2] + abs(h[i] - h[i - 2])  # cost2 には 2 後ろの dp の値と cost の絶対値
    cost1 = dp[i-1] + abs(h[i] - h[i - 1])  # cost1 には 1 後ろの dp の値と cost の絶対値
    dp[i] = min(cost2, cost1)               # 小さい方を dp に入れる


print(dp[N])