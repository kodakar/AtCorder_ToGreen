N = int(input())
P = [*map(int, input().split())]

if N == 1:
    print(0)
else:
    print(max(0, max(P[1:])-P[0]+1))