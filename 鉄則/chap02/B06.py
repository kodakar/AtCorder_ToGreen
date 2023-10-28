N = int(input())
A = list(map(int, input().split()))
Q = int(input())

wl = [[0, 0] for _ in range(N)]

for i in range(N):
    if A[i] == 0:
        wl[i][0] += 1
    else:
        wl[i][1] += 1

wl = [[0,0]] + wl

for i in range(1, N+1):
    wl[i][0] += wl[i-1][0]
    wl[i][1] += wl[i-1][1]

for i in range(Q):
    L, R = map(int, input().split())

    lose = wl[R][0] - wl[L-1][0]
    win = wl[R][1] - wl[L-1][1]

    if lose < win:
        print("win")
    elif lose == win:
        print("draw")
    else:
        print("lose")
    
        