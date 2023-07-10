S = input()
T = ""
l = len(S)

while True:
    if S[l-5:l] == "dream" or S[l-5:l] == "erase":
        l -= 5
    elif S[l-6:l] == "eraser":
        l -= 6
    elif S[l-7:l] == "dreamer":
        l -= 7
    else:
        print("NO")
        exit()
    if l == 0:
        print("YES")
        exit()

  