n, m = map(int, input().split())

fr = [[i] for i in range(n)]

for _ in range(m):
    x, y = map(int, input().split()) 
    fr[x - 1].append(y - 1)
    fr[y - 1].append(x - 1)

num = 0

for i in range(1 << n):
    count = 0
    fr2 = [True for _ in range(n)]
    for shift in range(n):
        if i >> shift & 1 == 1:
            count += 1
            # member.append(shift)
            for j in range(n):
                if shift not in fr[j]:
                    fr2[j] = False
    
        # print(i, shift, fr2, count)
    if count == fr2.count(True):
        num = max(num, fr2.count(True))

print(num)