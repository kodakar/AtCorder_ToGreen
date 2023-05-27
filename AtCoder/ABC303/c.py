N, M, H, K = map(int, input().split())
S = input()

a = set()

for i in range(M):
    x, y = map(int, input().split())
    a.add((x, y))

x, y = (0, 0)

count = 0

for i in S:
    count += 1
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1

    H -= 1

    if H < 0:
        print("No")
        exit()

    if (x, y) in a and H < K:
        H = K
        a.remove((x, y))
    
    if N <= count:
        print("Yes")
        exit()