N, K = map(int, input().split())

for i in range(31):
    if N < K**i:
        print(i)
        break
    elif N == K**i:
        print(i+1)
        break