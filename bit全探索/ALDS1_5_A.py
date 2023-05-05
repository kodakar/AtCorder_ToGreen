n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

answers = []

for i in range(1 << n):
    ans = 0

    for shift in range(n):
        if i >> shift & 1 == 1:
            ans += a[shift]

    answers.append(ans)

for i in range(q):
    if m[i] in answers:
        print("yes")
    else:
        print("no")

# print(answers)