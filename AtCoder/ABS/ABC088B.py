N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0

# print(a)

for i in range(len(a)):
    if i % 2 == 0:
        Alice += max(a)
        a.remove(max(a))
    else:
        Bob += max(a)
        a.remove(max(a))
    # print(a)

print(Alice - Bob)