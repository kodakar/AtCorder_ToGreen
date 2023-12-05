N = int(input())
v = list(map(int, input().split()))
v.sort()
# print(v)
while len(v) > 1:
    v[:2] = [(v[0] + v[1])/2]
print(v[0])
