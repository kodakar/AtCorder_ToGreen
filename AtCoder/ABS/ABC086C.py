N = int(input())

pre_t = 0
pre_x = 0
pre_y = 0
flag = True

for _ in range(N):
    t, x, y = map(int, input().split())
    d = abs(x - pre_x) + abs(y - pre_y)
    time = t - pre_t

    pre_t = t
    pre_x = x
    pre_y = y

    if time < d:
        flag = False
    elif time % 2 != d % 2:
        flag = False

if flag:
    print("Yes")
else:
    print("No")