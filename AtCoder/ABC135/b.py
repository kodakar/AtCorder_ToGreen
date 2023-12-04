N = int(input())
p = list(map(int, input().split()))

cnt = 0

p2 = sorted(p)

for i in range(N):
    if p[i] != p2[i]:
        cnt += 1

if cnt <= 2:
    print("YES")
else:
    print("NO")