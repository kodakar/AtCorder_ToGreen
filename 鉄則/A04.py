N = int(input())
s = ""
for shift in range(10):
    s += str(N >> shift & 1)
print(s[::-1])