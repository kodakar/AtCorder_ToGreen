N, M = map(int, input().split())
S = input()
T = input()

if T[0:N] == S and T[len(T)-N:len(T)] == S:
    print(0)
elif T[0:N] == S:
    print(1)
elif T[len(T)-N:len(T)] == S:
    print(2)
else:
    print(3)
