N = int(input())

matrix = [[0] * N for _ in range(N)]

left, right, top, bottom = 0, N - 1, 0, N - 1
num = 1

while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

matrix[N//2][N//2] = "T"

for row in matrix:
        print(*row)
