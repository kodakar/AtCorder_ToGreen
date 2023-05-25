S = input()

B_pos = []
R_pos = []

for i in range(8):
    if S[i] == "B":
        B_pos.append(i + 1)
    elif S[i] == "R":
        R_pos.append(i + 1)
    elif S[i] == "K":
        K = i + 1

if (B_pos[0] % 2 == 0 and B_pos[1] % 2 != 0) or (B_pos[0] % 2 != 0 and B_pos[1] % 2 == 0):
    if R_pos[0] < K < R_pos[1]:
        print("Yes")
        exit()

print("No")