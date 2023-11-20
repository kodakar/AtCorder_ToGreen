S = input()
alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if len(S) != 8 or S[0] not in alp or S[-1] not in alp or S[1] == "0":
    print("No")
    exit()

for i in range(1, len(S)-1):
    if S[i] in alp:
        print("No")
        exit()

print("Yes")