A, B, X = map(int, input().split())

L = 0
R = 10**9 + 1

while L + 1 != R:
    N = (L+R)//2

    if X < A * N + B * len(str(N)):
        R = N
    else:
        L = N

print(L)
