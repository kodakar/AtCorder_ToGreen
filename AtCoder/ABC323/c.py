N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

now_points = [0 for _ in range(N)]

nokori = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            now_points[i] += A[j]
        else:
            nokori[i].append(A[j])

for i in range(N):
    now_points[i] += i+1

# print(now_points)
# print(nokori)

top = max(now_points)

for i in range(N):
    cnt = 0
    if now_points[i] - top < 0:
        for j in (sorted(nokori[i], reverse=True)):
            if j + now_points[i] > top:
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1
                now_points[i] += j
    else:
        print(cnt)