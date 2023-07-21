S = list(map(int, input().split()))

if S == sorted(S):
    if 100 <= S[0] and S[7] <= 675:
        for i in S:
            if i % 25 == 0:
                print("Yes")
                exit()

print("No")