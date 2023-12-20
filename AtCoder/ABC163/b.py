N, M = map(int, input().split())
A = list(map(int, input().split()))
print(N - sum(A) if 0 <= N - sum(A) else -1)