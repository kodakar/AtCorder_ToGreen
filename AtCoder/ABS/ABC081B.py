n = int(input())
a = list(map(int,input().split()))
cnt = 0
while True:
    # print(a)
    isEven = True
    new_a = []
    for i in a:
        if i % 2 != 0:
            isEven = False
            break
    if isEven:
        for i in range(len(a)):
            new_a.append(a[i]//2)
        a = new_a
        cnt += 1
    else:
        break

print(cnt)