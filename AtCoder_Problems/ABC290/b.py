N, K = map(int, input().split())
S = list(input())

count = 0

for i in range(N):
    if count < K:
        if S[i] == "o":
            count += 1
    else:
        if S[i] == "o":
            S[i] = "x"

print("".join(S))
