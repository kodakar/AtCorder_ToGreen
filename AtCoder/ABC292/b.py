N, Q = map(int, input().split())

P = [0 for _ in range(N)]

for i in range(Q):
    e = list(map(int, input().split()))
    if e[0] == 1:
        P[e[1]-1] += 1
    elif e[0] == 2:
        P[e[1]-1] += 2
    else:
        if P[e[1]-1] > 1:
            print("Yes")
        else:
            print("No")
