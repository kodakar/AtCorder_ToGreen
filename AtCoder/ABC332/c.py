N, M = map(int, input().split())
S = input().split("0")
a = []
for i in S:
    if i != "":
        a.append(list(i))

ans = 0

for s in a:
    T = M
    cnt = 0
    for i in range(len(s)):
        if s[i] == "1":
            if T <= 0:
                cnt += 1
            else:
                T -= 1
        else:
            cnt += 1
    ans = max(ans, cnt)

print(ans)