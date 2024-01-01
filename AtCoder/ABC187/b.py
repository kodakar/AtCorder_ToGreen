N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        if -1 <= (XY[j][1] - XY[i][1])/(XY[j][0] - XY[i][0]) <= 1:
            ans += 1
print(ans)