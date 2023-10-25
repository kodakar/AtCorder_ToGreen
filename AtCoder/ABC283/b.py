N = int(input())
A = [*map(int, input().split())]
Q = int(input())

for i in range(Q):
    q = [*map(int, input().split())]
    if len(q) == 2:
        print(A[q[1]-1])
    else:
        A[q[1]-1] = q[2]