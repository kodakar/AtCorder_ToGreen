import math
H, W = map(int, input().split())
print(math.comb(H+W-2,W-1)%(7+10**9))