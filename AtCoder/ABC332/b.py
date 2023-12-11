K, G, M = map(int, input().split())

q = [0] * 2

for i in range(K):
    if q[0] >= G:
        q[0] = 0
    elif q[1] == 0:
        q[1] = M
    else:
        for j in range(G):
            q[0] += 1
            q[1] -= 1
            if q[0] >= G or q[1] == 0:
                break
    # print(q)

print(*q)