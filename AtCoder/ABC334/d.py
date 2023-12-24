from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))

R.sort()

need = [0 for _ in range(N)]
need[0] = R[0]

for i in range(1,N):
    need[i] = need[i-1] + R[i]

for i in range(Q):
    q = int(input())
    print(bisect_right(need,q))