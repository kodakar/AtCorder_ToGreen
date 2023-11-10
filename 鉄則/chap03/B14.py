import bisect

def bit(A):
    sumList = []
    for i in range(2 ** len(A)):
        sum = 0
        for shift in range(len(A)):
            if i >> shift & 1 == 1:
                sum += A[shift]
        sumList.append(sum)
    return sumList

N, K = map(int, input().split())
A = list(map(int, input().split()))

C1 = A[:N//2]
C2 = A[N//2:]

C1_sum = sorted(bit(C1))
C2_sum = sorted(bit(C2))

for i in range(len(C1_sum)):
    pos = bisect.bisect_left(C2_sum, K - C1_sum[i])
    if pos < len(C2_sum) and C2_sum[pos] == K - C1_sum[i]:
        print("Yes")
        exit()

print("No")

