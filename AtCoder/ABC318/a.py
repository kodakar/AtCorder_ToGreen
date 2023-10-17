N, M, P = map(int, input().split())

v = []

for i in range(10**10):
    if M + (i * P) > N:
        break
    v.append(M+i*P)

print(len(v))
