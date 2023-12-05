N = int(input())
A = list(map(int, input().split()))
a = 0
for i in A:
    a += 1/i
print(1/a)
