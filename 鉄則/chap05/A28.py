N = int(input())
ans = 0
for i in range(N):
    T, A = map(str, input().split())
    A = int(A)

    if T == "+":
        ans += A
    elif T == "-":
        ans -= A
    elif T == "*":
        ans *= A
        
    if ans < 0:
        ans += 10000

    ans %= 10000 

    print(ans)