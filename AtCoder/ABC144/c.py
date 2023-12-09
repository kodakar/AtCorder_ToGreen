import math

N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

a = make_divisors(N)

ans = float("inf")

for i in range(math.ceil(len(a)/2)):
    ans = min(ans, a[i] + a[-i-1] - 2)

print(ans)