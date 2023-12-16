import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i, n in enumerate(list(itertools.permutations([i for i in range(1, N+1)]))):
    if P == list(n):
        a = i
    if Q == list(n):
        b = i

print(abs((a+1)-(b+1)))