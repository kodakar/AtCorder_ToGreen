T = int(input())
N = int(input())

num = [0 for _ in range(T+1)]

for i in range(N):
    L, R = map(int, input().split())
    num[L] += 1
    num[R] -= 1

for i in range(1, T):
    num[i] += num[i-1]

for i in range(T):
    print(num[i])