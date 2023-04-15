n, x = map(int, input().split())

now_a = 0

for i in range(n):
    v, p = map(int, input().split())
    now_a += v * p

    if x * 100 < now_a:
        print(i+1)
        exit()

print(-1)