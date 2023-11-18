N = int(input())
S = input()

dic = {i:0 for i in (set(S))}

a = ""

for s in S:
    if a == "" or a[0] == s:
        a += s
        dic[a[0]] = max(dic[a[0]], len(a))
    else:
        dic[a[0]] = max(dic[a[0]], len(a))
        a = s

print(sum(dic.values()))