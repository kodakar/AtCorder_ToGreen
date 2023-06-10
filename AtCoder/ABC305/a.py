n = input()

if 0 <= int(n[-1]) <= 2:
    print(n[0:len(n) - 1] + "0")
elif 3 <= int(n[-1]) <= 7:
    print(n[0:len(n) - 1] + "5")
else:
    if len(n) == 1:
        print(10)
    else:
        print(str(int(n[0:len(n) - 1]) + 1 ) + "0")