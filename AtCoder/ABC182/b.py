N = int(input())
A = list(map(int, input().split()))

ans = -10**10
ans2 = 0

for i in range(2, max(A)+1):
    cnt = 0
    for j in A:
        if j % i == 0:
            cnt += 1
    if cnt >= ans:
        ans = cnt
        ans2 = i
        

print(ans2)