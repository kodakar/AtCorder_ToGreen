N = int(input())
S = [input() for _ in range(N)]

a = set()
no = 0
tmp = len(a)

for s in S:
    a.add(s)
    if s != s[::-1]:
        a.add(s[::-1])
    # print(tmp, len(a),s)
    if tmp != len(a):
        no += 1
    tmp = len(a)
print(no)