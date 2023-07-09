while True:
    s = input()
    if s == "-":
        exit()
    m = int(input())
    h = [int(input()) for _ in range(m)]
    for i in h:
        s = s[i:] + s[:i]

    print(s)