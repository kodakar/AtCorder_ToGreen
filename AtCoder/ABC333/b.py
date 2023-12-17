S = sorted(input())
T = sorted(input())

S1, S2 = S[0], S[1]
T1, T2 = T[0], T[1]

A = ["A","B","C","D","E"]

if A.index(S2) - A.index(S1) == A.index(T2) - A.index(T1):
    print("Yes")
elif A.index(S2) - A.index(S1) == 2 and A.index(T2) - A.index(T1) == 3:
    print("Yes")
elif A.index(S2) - A.index(S1) == 3 and A.index(T2) - A.index(T1) == 2:
    print("Yes")
elif A.index(S2) - A.index(S1) == 4 and A.index(T2) - A.index(T1) == 1:
    print("Yes")
elif A.index(S2) - A.index(S1) == 1 and A.index(T2) - A.index(T1) == 4:
    print("Yes")
else:
    print("No")