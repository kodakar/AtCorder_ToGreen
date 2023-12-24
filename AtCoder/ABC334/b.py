A, M, L, R = map(int, input().split())

if L <= A <= R:
    print(abs(A-L)//M + abs(A-R)//M + 1)
elif A <= L:
    print(abs(A-R)//M - abs(A-(L-1))//M)
elif R <= A:
    print(abs(A-L)//M - abs(A-(R+1))//M)