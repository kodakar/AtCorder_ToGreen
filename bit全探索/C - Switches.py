N, M = map(int, input().split())

k = []

for i in range(M):
    a = list(map(int, input().split()))
    k.append(a[1:])

p = list(map(int, input().split()))

ans = 0

for i in range(1 << N):
    on = [0 for _ in range(M)]
    flash = [False for _ in range(M)]
    for shift in range(N):
        if i >> shift & 1 == 1:
            for j in range(M):
                # print(shift + 1, k[j], p[j])
                if shift + 1 in k[j]:
                    on[j] += 1 
    
    for j in range(M):
        if on[j] != 0 and on[j] % 2 == p[j]:
            flash[j] = True

    # print("  on :", on)
    # print("flash:", flash)
    if False not in flash:
        ans += 1
    

print(ans)