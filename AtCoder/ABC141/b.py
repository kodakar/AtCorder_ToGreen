S = input()

for i in range(len(S)):
    if (i+1) % 2 == 0:
        if not (S[i] == "L" or S[i] == "U" or S[i] == "D"):
            print("No")
            exit()
    else:
        if not (S[i] == "R" or S[i] == "U" or S[i] == "D"):
            print("No")
            exit()


print("Yes")