A, B = map(int, input().split())

if abs(A-B)/2 == abs(A-B)//2:
    print(abs(A+B)//2)
else:
    print("IMPOSSIBLE")