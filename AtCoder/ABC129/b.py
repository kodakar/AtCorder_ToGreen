N = int(input())
W = list(map(int, input().split()))

ans = float("inf")

for t in range(N-1):
    S1 = W[:t+1]
    S2 = W[t+1:]
    ans = min(ans, abs(sum(S1)-sum(S2)))

print(ans)