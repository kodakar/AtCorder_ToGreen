N, A, B = map(int, input().split())
b = []
for i in range(1, N+1):
    a = list(map(int,str(i)))
    if A <= sum(a) <= B:
        b.append(i)
        # print(b)

print(sum(b))