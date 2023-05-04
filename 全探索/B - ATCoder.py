s = input()

ACGT = False

count = 0

ans = 0

for i in s:
    if ACGT == True and (i == "A" or i == "C" or i == "G" or i == "T"):
        count += 1

    if ACGT == False and (i == "A" or i == "C" or i == "G" or i == "T"):
        ACGT = True
        count += 1

    ans = max(ans, count)

    if not (i == "A" or i == "C" or i == "G" or i == "T"):
        count = 0
        ACGT = False
    

print(ans)