S = input()

def YY(s):
    if (0 <= int(s[0]) <= 9) and (0 <= int(s[1]) <= 9):
        return True
    return False

def MM(s):
    if ((0 == int(s[0])) and (1 <= int(s[1]) <= 9)) or ((1 == int(s[0])) and (0 <= int(s[1]) <= 2)):
        return True
    return False

s1 = S[:2]
s2 = S[2:]

if (YY(s1) and MM(s2)) and (MM(s1) and YY(s2)):
    print("AMBIGUOUS")
elif YY(s1) and MM(s2):
    print("YYMM")
elif MM(s1) and YY(s2):
    print("MMYY")
else:
    print("NA")


