N = int(input())
L = list(map(int, input().split()))

ans = 0

for i in range(len(L)):
    for j in range(i+1, len(L)):
        for k in range(j+1, len(L)):
            a = L[i]
            b = L[j]
            c = L[k]
            if a != b and b != c and c != a:
                if a + b > c and b + c > a and c + a > b:
                    ans += 1
print(ans)