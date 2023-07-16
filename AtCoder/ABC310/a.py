n, p, q= map(int, input().split())
d = list(map(int, input().split()))

if p > q + min(d):
    print(q + min(d))
else:
    print(p)
