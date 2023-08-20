S = input()
a = ["a", "e", "i","o","u"]

s = ""
for i in S:
    if i not in a:
        s += i

print(s)