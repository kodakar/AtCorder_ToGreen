N = int(input())
A = set()
for i in range(1,13):
    for j in range(1,13):
        for k in range(1,13):
            A.add(int("1" * i) + int("1" * j) + int("1" * k))

A = sorted(A)

print(A[N-1])