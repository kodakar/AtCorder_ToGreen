N, Q = map(int, input().split())
S = input()

cnt = [0]
for i in range(1, N):
    if S[i-1] == S[i]:
        cnt.append(cnt[i-1] + 1)
    else:
        cnt.append(cnt[i-1])

for i in range(Q):
    l, r = map(int, input().split())
    print(cnt[r-1] - cnt[l-1])
