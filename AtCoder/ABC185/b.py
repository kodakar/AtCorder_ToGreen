N, M, T = map(int, input().split())

now_t = 0
now_n = N

for i in range(M):
    A, B = map(int, input().split())
    now_n -= A - now_t
    if now_n <= 0:
        print("No")
        exit()
    # print(N)
    now_n += B - A
    if N <= now_n:
        now_n = N
    now_t = B
    # print(N)

now_n -= T - now_t

if now_n <= 0:
    print("No")
else:
    print("Yes")