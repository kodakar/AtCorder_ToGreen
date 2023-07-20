N, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

A.sort()

sum = 0

for i in A:
    sum += i[1]

if sum <= K:
    print(1)
    exit()

for a, b in A:
    sum -= b
    if sum <= K:
        print(a+1)
        exit()