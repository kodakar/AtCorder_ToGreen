N, X = map(int, input().split())
# A = list(map(int, input().split()))
A = set(map(int, input().split()))

B = A.copy()

if X == 0:
    print("Yes")
    exit()

for i in range(len(A)):
    if A.pop() - X in B:
        print("Yes")
        exit()

print("No")