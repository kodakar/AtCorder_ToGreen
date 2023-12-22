N = int(input())
L = list(map(int, input().split()))
print(L)
ans = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] != L[k]:
                if abs(L[i]-L[j]) < L[k] < L[i] + L[j]:
                    ans.append(sorted([L[i],L[j],L[k]]))
print((ans))