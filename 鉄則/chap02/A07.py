# numpy ver ------------------

# import numpy as np

# D = int(input())
# N = int(input())

# atd = np.array([0 for _ in range(D)])

# for i in range(N):
#     L, R = map(int, input().split())
#     atd[L-1:R] += 1

# for i in atd:
#     print(i)

# normal ver ------------------

D = int(input())
N = int(input())

atd = [0 for _ in range(D+2)]

for i in range(N):
    L, R = map(int, input().split())
    atd[L] += 1
    atd[R + 1] -= 1

for i in range(1, D+1):
    atd[i] += atd[i - 1]

for i in range(1,D+1):
    print(atd[i])

