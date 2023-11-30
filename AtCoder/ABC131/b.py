N, L = map(int, input().split())
t = [L + (i + 1) - 1 for i in range(N)]
ans = 10**10
a = 0
for i in range(N):
    if ans > abs(sum(t)-(sum(t[:i])+sum(t[i+1:]))):
        ans = abs(sum(t)-(sum(t[:i])+sum(t[i+1:])))
        a = sum(t[:i])+sum(t[i+1:])
print(a)