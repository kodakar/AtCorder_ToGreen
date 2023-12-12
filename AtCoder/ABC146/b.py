import bisect 

N = int(input())
S = input()

a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

b = []

for i in S:
    b.append(bisect.bisect_left(a,i)+N)

ans = []

for i in b:
    ans.append(a[i % 26])

print("".join(ans))