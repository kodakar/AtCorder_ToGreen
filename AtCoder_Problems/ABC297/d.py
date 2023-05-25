A, B = map(int, input().split())

ans = 0

while True:
    if A > B:
        if A % B != 0:
            ans += (A // B)
            A = A - B * (A // B)
        else:
            ans += (A // B) - 1
            A = A - B * ((A // B) - 1)
    elif A < B:
        if B % A != 0:
            ans += (B // A)
            B = B - A * (B // A)
        else:
            ans += (B // A) - 1
            B = B - A * ((B // A) - 1)
    else:
        print(ans)
        break
