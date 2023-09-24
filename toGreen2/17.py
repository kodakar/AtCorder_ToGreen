N = int(input())
num = set()

for a in range(2, 10**5):
    for b in range(2, 1000):
        if a ** b <= N:
            num.add(a**b)
        else:
            break

print(N-len(num))