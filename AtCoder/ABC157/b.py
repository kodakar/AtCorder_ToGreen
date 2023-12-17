A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

for i in B:
    for j in range(3):
        for k in range(3):
            if i == A[j][k]:
                A[j][k] = 0

for i in range(3):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    for j in range(3):
        if A[i][j] == 0:
            cnt1 += 1
        if A[j][i] == 0:
            cnt2 += 1
        if A[j][j] == 0:
            cnt3 +=1
        if A[j][-(j+1)] == 0:
            cnt4 += 1
    if cnt1 == 3 or cnt2 == 3 or cnt3 == 3 or cnt4 == 3:
        print("Yes")
        exit()

print("No")