N = int(input())
A, B, C = map(int, input().split())

ans = 9999

for i in range(10000):
    for j in range(10000 - i):
        k = N - (A * i + B * j)
        if k < 0:
            break
        if k % C == 0:
            k = k//C
            ans = min(ans,i + j + k)

print(ans)