n = int(input())

def yakusu(n):
    y = []
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            y.append(i)
            if i != n//i:
                y.append(n//i)
        i += 1

    y.sort()
    return y

ans = yakusu(n)

for i in ans:
    print(i)