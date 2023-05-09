a, b, c, x, y = map(int, input().split())

# if a + b <= 2 * c:
#     print(a * x + b * y)

# else:
#     if x <= y:
#         print(min(2 * c * y, 2 * c * x + b * (y - x)))
#     else:
#         print(min(2 * c * x, 2 * c * y + a * (x - y)))

ans = 2*(5000*10**5)

for z in range(10 ** 5 + 1):
    total = a * max(x - z, 0) + b * max(y - z, 0) + 2 * c * z
    ans = min(total,ans)
print(ans)