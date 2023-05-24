N = int(input())
A = list(map(int, input().split()))

m = [0 for _ in range(200)]

for i in range(N):
    tmp = A[i] % 200
    m[tmp] += 1

ans = 0

for j in range(200):
    num = m[j] - 1
    if num > 0:
        ans += num * (num + 1) // 2     # k * (k - 1) // 2 は k 個のものから r 個のものを選ぶ組み合わせ式

print(ans)