N = int(input())
S = input()

for i in range(1, N):
    if S[i] == S[i - 1]:
        print("No")
        exit()

print("Yes") 