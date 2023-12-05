import math

N = int(input())

dic = {}

for i in range(N):
    s = list(input())
    s = "".join(sorted(s))
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

ans = 0

if len(dic) != N:
    for i in dic:
        if dic[i] > 1:
            ans += math.comb(dic[i],2)
            
print(ans)
