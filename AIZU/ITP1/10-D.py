n = int(input())
x = list(map(float, input().split()))
import math

y = list(map(float, input().split()))

for i in range(4):
    if i == 0:
        ans = 0
        for j in range(n):
            ans += abs(x[j] - y[j])
        print(ans)
    elif i == 1:
        ans = 0
        for j in range(n):
            ans += abs(x[j] - y[j]) ** 2
        print(ans ** (1/2))
    elif i == 2:
        ans = 0
        for j in range(n):
            ans += abs(x[j] - y[j]) ** 3
        print(ans ** (1/3))
    else:
        ans = 0
        for j in range(n):
            tmp = abs(x[j] - y[j])
            ans = max(ans,tmp)
        print(ans)
