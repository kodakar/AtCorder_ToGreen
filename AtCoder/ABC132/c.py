import bisect

N = int(input())
d = list(map(int, input().split()))
d.sort()
ans = 0

for i in range(1,1 + 10**5):
    if bisect.bisect_left(d,i) == N//2:
        ans += 1
print(ans)
