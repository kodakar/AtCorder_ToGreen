n = int(input())

able_num = set()

for a in range(2, 10**5 + 10):
    for b in range(2, 1000):
        if a ** b <= n:
            able_num.add(a**b)
        else:
            break

print(n-len(able_num))