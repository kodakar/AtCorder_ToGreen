N = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(D[i]+1):
        num = str(i+1) + str(j)
        if len(set([*num])) == 1:
            ans += 1

print(ans)