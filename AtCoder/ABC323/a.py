S = input()

for i,s in enumerate(S):
    if (i+1) % 2 == 0 and s != "0":
        print("No")
        exit()

print("Yes")


