w = input()
t = []

while True:
    T = list(input().split())
    if T[0] == "END_OF_TEXT":
        break
    t += T

ans = 0

for i in t:
    if i.lower() == w.lower():
        ans += 1

print(ans)