A, B = map(int, input().split())
ans = 1
i = 0
while ans < B:
    ans += A - 1
    i += 1
    # print(ans)
print(i)