N, K = map(int, input().split())
M = []
for i in range(N):
    A, B = map(int, input().split())
    M.append([A, B])
M.sort()
# print(M)
now = 0

now += K

for i in range(N):
    if M[i][0] <= now:
        now += M[i][1]

print(now)