S = input()

a = ["ACE","BDF","CEG","DFA","EGB","FAC","GBD"]

for i in a:
    if i == S:
        print("Yes")
        exit()

print("No")