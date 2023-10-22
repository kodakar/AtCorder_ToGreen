T = int(input())

for i in range(T):
    N = int(input())
    A = [*map(int, input().split())]
    cnt = 0
    for i in range(N):
        if A[i] % 2 != 0:
            cnt += 1
    print(cnt)