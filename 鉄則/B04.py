N = [*input()]
ans = 0
for i in range(len(N)):
    num = N[::-1]
    if num[i] == "1":
        ans += 2 ** i
print(ans)