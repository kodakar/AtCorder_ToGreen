N = int(input())
A = []
for i in range(N):
    F, N = map(int, input().split())
    A.append([N, F])
A.sort(reverse=True)

ans = A[0][0]

if A[0][1] != A[1][1]:
    print(ans + A[1][0])
    exit()
else:
    ans += A[1][0]//2

new_ans = A[0][0]

# print(A)

for i in range(len(A)):
    if A[0][1] != A[i][1]:
        new_ans += A[i][0]
        if ans < new_ans:
            print(new_ans)
        else:
            print(ans)
        exit()

print(ans)