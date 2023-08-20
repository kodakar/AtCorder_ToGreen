import math

A, B = map(int, input().split())

def lcm(a, b):
    return  (a * b)//math.gcd(a, b)

# math.lcm は python3.9 以上

print(lcm(A, B))