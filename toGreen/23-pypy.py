N = int(input())
A = list(map(int, input().split()))

#　最大値をかなり小さい数で用意
ans = -10 ** 15

for l in range(N):
    A_min = A[l]                               # l番目を最小値とする
    for r in range(1, N):                      
        A_min = min(A_min, A[r])               # l番目 から r番目 の中の最小値を見つける
        ans = max(ans, A_min * (r - l + 1))    # l番目 から r番目 の最小値を l ~ r の個数分かける

print(ans)

