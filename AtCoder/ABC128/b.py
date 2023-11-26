N = int(input())

ans = []

for i in range(N):
    S, P = map(str, input().split())
    ans.append([S, -int(P), i+1])

ans.sort()

for i in range(N):
    print(ans[i][2])