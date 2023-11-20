Q = int(input())

def prime_check(x):
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return print("No")
    return print("Yes")

for i in range(Q):
    X = int(input())
    prime_check(X)