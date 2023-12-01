S = list(input())
a = set(S)
b = set(S[:2])
c = set(S[2:])

if len(a) == 2:
    if len(b) == len(c) == 1 or len(b) == len(c) == 2:
        print("Yes")
        exit()

print("No")