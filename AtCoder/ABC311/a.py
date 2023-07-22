N = int(input())
S = list(input())

a = [False] * 3

for i in range(N):
    if S[i] == "A":
        a[0] = True
    elif S[i] == "B":
        a[1] = True
    elif S[i] == "C":
        a[2] = True

    if False not in a:
        print(i+1)
        exit()