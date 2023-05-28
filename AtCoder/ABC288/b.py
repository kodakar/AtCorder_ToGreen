N, K = map(int, input().split())
s = [input() for _ in range(N)]
S = []
for i in range(K):
    S.append(s[i])

S = sorted(S)

for i in S:
    print(i)