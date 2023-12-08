N = int(input())
S = input()

a = S[0]

for i in range(1, N):
    if a[-1] != S[i]: 
        a += S[i]
        
print(len(a))