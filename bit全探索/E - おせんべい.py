import numpy as np

R, C = map(int, input().split())

a = np.array([list(map(int, input().split())) for _ in range(R)])

ans = 0

for i in range(1 << R):
    b = a.copy()
    for j, aj in enumerate(a):
        num = (i >> j) & 1
        b[j] = aj ^ num
    
    cnt = b.sum(axis=0)
    chk = np.maximum(cnt, R - cnt).sum()
    ans = max(ans,chk)
    
print(ans)