A = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    if len(set(A[i])) != len(A[i]):
        print("No")
        exit()

for i in range(9):
    a = []
    for j in range(9):
        a.append(A[j][i])
    if len(a) != len(set(a)):
        print("No")
        exit()
    
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        a = A[i][j:j+3] + A[i+1][j:j+3] + A[i+2][j:j+3]
        if len(a) != len(set(a)):
            print("No")
            exit()

print("Yes")

