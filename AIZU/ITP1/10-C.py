import math
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(float, input().split()))
    m = sum(a)/n
    b = 0
    for i in a:
        b += (i - m) ** 2
    std = b/n
    print(math.sqrt(std))
