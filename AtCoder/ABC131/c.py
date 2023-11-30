import math

A, B, C, D = map(int, input().split())

E = math.lcm(C, D)
A -= 1
print((B - B//C - B//D + B//E)-(A - A//C - A//D + A//E))