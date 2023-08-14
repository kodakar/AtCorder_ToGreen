N = int(input())
ans = []

for i in range(N):
    S, T = input().split()
    T = int(T)
    ans.append([T, S])

print(sorted(ans,reverse=True)[1][1])
