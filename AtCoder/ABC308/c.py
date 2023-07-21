N = int(input())

a = []

for i in range(N):
    A, B = map(int, input().split())
    a.append([(10**19*A//(A+B)), -i-1])         # -i - 1 にする事で、確率が同じ時に昇順になる 10**19*A//(A+B) で不動小数点対策

ans = []
for i in sorted(a, reverse=True):
    ans.append(-i[1])

print(*ans)