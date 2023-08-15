N, K = map(int, input().split())

def g1(x):
    tmp = list(str(x))
    return int("".join(sorted(tmp, reverse=True)))

def g2(x):
    tmp = list(str(x))
    return int("".join(sorted(tmp)))

def f(x):
    return g1(x) - g2(x)

x = N
for i in range(K):
    x = f(x)

print(x)