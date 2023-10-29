N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
    num  = 0
    for i in range(N):
        num += x//A[i]
    if K <= num:
        return True
    return False

L = 1
R = 10**9
mid = (R + L)//2

while True:
    if check(mid) == True:
        R = mid
    else:
        L = mid + 1
    mid = (L + R)//2
    if R <= L:
        print(L)
        break