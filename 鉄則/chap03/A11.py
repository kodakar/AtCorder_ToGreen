N, X = map(int, input().split())
A = list(map(int, input().split()))

a = len(A)//2
L = 0
R = len(A)-1
cnt = 0

while True:
    if X < A[a]:
        R = a - 1
    elif A[a] < X:
        L = a + 1
    else:
        print(a+1)
        break
    a = (R + L)//2
    