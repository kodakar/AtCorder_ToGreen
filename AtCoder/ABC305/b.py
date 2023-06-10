p, q = input().split()

a = ["A", "B", "C", "D", "E", "F", "G"]
b = [3,1,4,1,5,9]

c = sorted([p, q])

flag = False

ans = 0

for i, j in enumerate(a):
    if j == c[0]:
        flag = True
    if j == c[1]:
        flag = False
    if flag:
        ans += b[i]

print(ans)