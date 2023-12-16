A, B, K = map(int, input().split())

if A <= K:
    B -= K - A
    A = 0
    if B < 0:
        B = 0 
else:
    A -= K
 
print(A, B)