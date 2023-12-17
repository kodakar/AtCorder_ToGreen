from math import comb
N, M = map(int, input().split())
print(comb(N,2) + comb(M,2))

