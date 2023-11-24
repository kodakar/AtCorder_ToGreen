N = int(input())
A = list(map(int, input().split()))

XOR = A[0]

for i in range(1,N):
    XOR = XOR ^ A[i]

print("Second" if XOR == 0 else "First")