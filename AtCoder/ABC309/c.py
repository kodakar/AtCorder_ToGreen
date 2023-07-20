N, K = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]

a.sort()

sum = 0

for i in a:
    sum += i[1]

if sum <= K:
    print(1)
    exit()

for i in range(len(a)):
    print(sum,K)
    if sum <= K:
        print(a[i-1][0]+1)
        exit()
    sum -= a[i][1]