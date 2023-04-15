import math

a, b = map(int, input().split())

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

print(lcm(a,b))