N = int(input())
S = input()

for i in range(1, N):
    for j in range(N):
        if i + j < len(S):
            if S[j] == S[i + j]:   
                print(j)
                break
        else:
            print(j)
            break