N = int(input())
A = [int(input()) for _ in range(N)]

pre_sum = [A[0]]
post_sum = [A[N-1]]

for i in range(1, N):
    pre_sum.append(max(A[i], pre_sum[i-1]))
    post_sum.append(max(A[-i-1],post_sum[i-1]))

post_sum.reverse()
# print(pre_sum, post_sum)

for i in range(N):
    if i == 0:
        print(post_sum[i+1])
    elif i == N - 1:
        print(pre_sum[i-1])
    else:
        print(max(pre_sum[i-1],post_sum[i+1]))