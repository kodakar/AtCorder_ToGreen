N, K = map(int, input().split())
sunuke = [0 for i in range(N+1)]
for i in range(K):
    d = input()
    A = list(map(int, input().split()))
    for i in A:
        sunuke[i] += 1
        
ans = 0

for i in sunuke[1:]:
    if i == 0:
        ans += 1
print(ans)