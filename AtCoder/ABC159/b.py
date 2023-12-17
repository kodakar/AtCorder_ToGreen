S = input()
print("Yes" if S == S[::-1] and S[:((len(S)-1)//2)] == S[:((len(S)-1)//2)][::-1] and S[((len(S)+3)//2)-1:] == S[((len(S)+3)//2)-1:][::-1] else "No")