N, K = map(int, input().split())
p = list(map(int, input().split()))

# 期待を入れる配列
p_ex = []

for i in range(N):
    p_ex.append((1 + p[i])/2)

# 区間和に使う配列　　[(0番目までの和), (1番目までの和), (2番目までの和), ... ,(n-1番目までの和), (n番目までの和)]
# 0 ~ n までの和は [n] で求められる。　k ~ n の和は [n] - [k - 1] で求められる。
p_ex_Cum = [p_ex[0]]

for i in range(1, N):
    p_ex_Cum.append(p_ex_Cum[i - 1] + p_ex[i])

ans = -10 ** 15

for i in range(N - K + 1):
    if i == 0:
        ans_temp = p_ex_Cum[i + K - 1]
    else:
        ans_temp = p_ex_Cum[i + K - 1] - p_ex_Cum[i - 1]

    ans = max(ans, ans_temp)

print(ans)