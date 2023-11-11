S = input()
ans = []
for i in range(len(S)):
    if S[i] == "C" and len(ans) >= 2:
        if ans[-2] == "A" and ans[-1] == "B":
            ans.pop()
            ans.pop()
            continue
    ans.append(S[i])
print("".join(ans))