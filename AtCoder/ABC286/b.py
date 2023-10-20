N = int(input())
S = [*input()]

ans = []
for i in range(len(S)):
    if S[i:i+2] == ["n","a"]:
        ans.append(S[i]+"y")
    else:
        ans.append(S[i])

print("".join(ans))