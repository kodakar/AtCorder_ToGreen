N = input()
pre_N = int(N[0])
for n in N[1:]:
    if pre_N <= int(n):
        print("No")
        exit()
    pre_N = int(n)
print("Yes")