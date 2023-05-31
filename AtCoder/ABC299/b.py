N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

mx = 10**-10
mx_index = 0

mx2 = C[0]
mx2_index = 1

for i in range(N):
    if C[i] == T:
        if mx < R[i]:
            mx = max(mx, R[i])
            mx_index = i + 1

    elif C[i] == C[0]:
        if mx2 < R[i]:
            mx2 = max(mx2, R[i])
            mx2_index = i + 1

if mx != 10**-10:
    print(mx_index)
else:
    print(mx2_index)
