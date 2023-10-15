N = int(input())
A = list(map(int, input().split()))
a = set(A)
if len(a) != 1:
    print("No")
else:
    print("Yes")