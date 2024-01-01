A, B  = map(str, input().split())
a = 0
b = 0
for i in range(len(A)):
    a += int(A[i])
    b += int(B[i])
print(a if b <= a else b)