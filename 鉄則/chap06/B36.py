N, K = map(int, input().split())
S = input()

ON = 0

for s in S:
    if s == "1":
        ON += 1

if abs(ON - K) % 2 == 0:
    print("Yes")
else:
    print("No")