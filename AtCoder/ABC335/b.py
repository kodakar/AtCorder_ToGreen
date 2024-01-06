N = int(input())
ans = []
for i in range(100):
    for j in range(100):
        for k in range(100):
            if i + j + k <= N:
                ans.append([i,j,k])

for i in sorted(ans):
    print(*i)