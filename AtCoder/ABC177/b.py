S = input()
T = input()

ans = -10**10

for i in range(len(S)-len(T) + 1):
    tmp = S[i:len(T)+i]
    same = 0
    for j in range(len(T)):
        if tmp[j] == T[j]:
            same += 1
    ans = max(ans, same)
    
print(len(T)-ans)