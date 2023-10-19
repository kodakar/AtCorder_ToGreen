N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(i+1,N):
        a = S[i] + S[j]
        b = S[j] + S[i]
        re_a = a[::-1]
        re_b = b[::-1]
        if a == re_a or b == re_b:
            print("Yes")
            exit()

print("No")
