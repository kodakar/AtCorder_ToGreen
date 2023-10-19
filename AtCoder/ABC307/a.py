n = int(input())
a = list(map(int, input().split()))

b = []
ans = 0
count = 0
for A in a:
    count += 1
    ans += A
    if count == 7:
        b.append((ans))
        ans = 0
        count = 0

print(*b)
    