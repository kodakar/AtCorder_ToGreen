n, k = map(int, input().split())

def func(n):
    return REV(n, True) - REV(n,False)


def REV(n, re):
    a = list(str(n))
    a.sort(reverse=re)
    a = "".join(a)
    return int(a)


for i in range(k):
    n = func(n)

print(n)