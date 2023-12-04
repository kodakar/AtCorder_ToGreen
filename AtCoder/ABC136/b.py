N = int(input())
ans = 0
for i in range(1,N+1):
    n = list(str(i))
    if len(n)%2 != 0:
        ans += 1
print(ans)