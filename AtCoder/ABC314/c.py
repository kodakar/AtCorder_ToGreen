N, M = map(int, input().split())
S = [*input()]
C = list(map(int, input().split()))

a = {}

tmp_s = []

for i in range(N):
    if C[i] not in a:
        a[C[i]] = [i]
    else:
        a[C[i]].append(i)
    
    tmp_s.append(S[i])

for i in range(1,M+1):
    for j in range(len(a[i])):
        tmp_s[a[i][j]] = S[a[i][j-1]]

print("".join(tmp_s))