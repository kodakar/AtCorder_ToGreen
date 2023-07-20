import copy

N = int(input())

A = [[int(i) for i in input()] for _ in range(N)]

new_A = copy.deepcopy(A)

for i in range(len(A)):
    for j in range(len(A[0])):
        if i == 0:
            if j == 0:
                new_A[i][j] = A[i+1][j]
            else:
                new_A[i][j] = A[i][j-1]
        elif i == len(A)-1:
            if j == len(A[0])-1:
                new_A[i][j] = A[i-1][j]
            else:
                new_A[i][j] = A[i][j+1]
        else:
            if j == 0:
                new_A[i][j] = A[i+1][j]
            elif j == len(A[0]) - 1:
                new_A[i][j] = A[i-1][j]

for i in new_A:
    for j in i:
        print(j, end="")
    print()