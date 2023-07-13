N = int(input())

ans = []

if N % 2 != 0:
    exit()

for i in range(1 << N):
    score = 0
    s = ""
    for shift in range(N):
        if i >> shift & 1 == 1:
            s += "("
            score += 1
        else:
            s += ")"
            score -=1
        if score < 0:
            break
    if score == 0:
        ans.append(s)
        # print(ans)

for i in sorted(ans):
    print(i)