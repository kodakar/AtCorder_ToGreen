N = int(input())

n_yaku = []
ans = ""

for i in range(1,N+1):
    if i > 9:
        break
    if N % i == 0:
        n_yaku.append(i)

for i in range(N+1):
    i_bai = []
    for j in n_yaku:
        if i % (N/j) == 0:
            i_bai.append(j)
    if i_bai: 
        ans += str(i_bai[0])
    else:
        ans += "-"

print(ans)