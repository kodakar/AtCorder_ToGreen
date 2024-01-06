N, Q = map(int, input().split())

head = [[i,0] for i in range(N,0,-1)]

for i in range(Q):
    n, q = map(str, input().split())
    n = int(n)
    if n == 1:
        if q == "R":
            head.append([head[-1][0] + 1, head[-1][1]])
        elif q == "L":
            head.append([head[-1][0] - 1, head[-1][1]])
        elif q == "U":
            head.append([head[-1][0], head[-1][1] + 1])
        elif q == "D":
            head.append([head[-1][0], head[-1][1] - 1])
    else:
        q = int(q)
        print(*head[-q])