N = int(input())

L = 0.0
R = 100.0

def f(x):
    return x**3 + x

for i in range(20):
    mid = (L+R)/2
    num = f(mid)
    if num < N:
        L = mid
    else:
        R = mid

print(mid)
