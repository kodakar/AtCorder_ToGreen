X, Y = map(int, input().split())

if X - Y < -2 or X - Y > 3:
    print("No")
else:
    print("Yes")