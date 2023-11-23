N = int(input())

a = [None] * (N + 1)

a[1] = 1
a[2] = 1

for i in range(3, N+1):
    a[i] = (a[i-1] + a[i-2]) % (7 + 10**9)

print(a[-1])