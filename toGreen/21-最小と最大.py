A, B, W = map(int, input().split())
W = W * 1000

MAX = -10 ** 15
MIN = 10 ** 15

for X in range(1, 10 ** 6 + 10):
    if A * X <= W <= B * X:
        MIN = min(MIN, X)
        MAX = max(MAX, X)

if MIN == 10**15:
    print("UNSATISFIABLE")
else:
    print(MIN, MAX)