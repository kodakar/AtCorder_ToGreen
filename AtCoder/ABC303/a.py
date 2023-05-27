n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i] == t[i]:
        continue
    else:
        if (s[i] == "l" and t[i] == "1") or (s[i] == "1" and t[i] == "l"):
            continue
        elif (s[i] == "o" and t[i] == "0") or (s[i] == "0" and t[i] == "o"):
            continue
        print("No")
        exit()

print("Yes")