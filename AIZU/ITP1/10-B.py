import math

a, b, d = map(float, input().split())
S = (1/2) * a * b * math.sin(math.radians(d))
L = math.sqrt((a ** 2) + (b ** 2) - 2 * a * b * math.cos(math.radians(d))) + a + b
h =  (S * 2) / a
print(S)
print(L)
print(h)