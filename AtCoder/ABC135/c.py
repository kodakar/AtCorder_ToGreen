N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    if A[i] - B[i] < 0:
        if A[i+1] - (B[i] - A[i]) < 0:
            ans += A[i] + A[i+1]
            A[i] = 0
            A[i+1] = 0
        else:
            ans += B[i]
            A[i+1] -= (B[i] - A[i])
            A[i] = 0
    else:
        ans += B[i]
        A[i] = A[i] - B[i]
    # print(A, ans)

print(ans)