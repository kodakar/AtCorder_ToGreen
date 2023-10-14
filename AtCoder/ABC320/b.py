S = [*input()]
ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        rev = S[i:j]
        if S[i:j] == rev[::-1]:
            ans = max(ans, len(S[i:j]))
print(ans)