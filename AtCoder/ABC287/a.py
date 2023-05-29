N = int(input())

a = 0

for i in range(N):
    S = input()
    if S == "For":
        a += 1

if a > N // 2:
    print("Yes")
else:
    print("Np")