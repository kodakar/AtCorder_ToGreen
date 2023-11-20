import math
A, B = map(int, input().split())

print((A*B)//math.gcd(A, B)) # python3.9 未満

print(math.lcm(A, B)) # python3.9 以降