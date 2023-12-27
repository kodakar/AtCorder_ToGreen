N = int(input())
x = list(map(int, input().split()))

m = 0
u = 0
c = -10**10

for i in range(N):
    m += abs(x[i])
    u += x[i]**2
    c = max(c, abs(x[i]))

print(m)
print(u**0.5)
print(c)