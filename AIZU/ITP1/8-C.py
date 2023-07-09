import sys

a = {}
tmp = "abcdefghijklmnopqrstuvwxyz"
for i in tmp:
    a[i] = 0


s = sys.stdin.read()

for j in s:
    if j.lower() in a:
        a[j.lower()] += 1


for i,j in zip(a.keys(), a.values()):
    print(str(i) + " : " + str(j))