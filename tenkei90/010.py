N = int(input())

ans1 = [0]
ans2 = [0]

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        ans1.append(ans1[i] + P)
        ans2.append(ans2[i])
    else:
        ans2.append(ans2[i] + P)
        ans1.append(ans1[i])


Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    print(ans1[R]-ans1[L-1], ans2[R]-ans2[L-1])