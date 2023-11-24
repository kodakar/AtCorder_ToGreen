N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

# print((((B * N) + sum(A)) * M + (sum(C) * N)))

print((sum(A) * M) + (B * N * M) + (sum(C) * N))