N, H, K = map(int, input().split())
P = list(map(int, input().split()))

for i, p in enumerate(P):
    if H + p >= K:
        print(i+1)
        exit()