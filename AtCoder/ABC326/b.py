N = int(input())

for i in range(N, 1000):
    n2s = str(i)
    if int(n2s[0]) * int(n2s[1]) == int(n2s[2]):
        print(n2s)
        exit()