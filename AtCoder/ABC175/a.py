S = input()
ans = [0 for _ in range(3)]
ans[0] = 1 if S[0] == "R" else 0
for i in range(1,3):
    if S[i] == "R":
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = 0

print(max(ans))