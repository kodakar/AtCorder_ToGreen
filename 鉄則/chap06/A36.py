N, K = map(int, input().split())

if K - ((N - 1) * 2) >= 0:
    if (K - ((N - 1) * 2)) % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")