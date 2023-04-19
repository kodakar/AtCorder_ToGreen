N, M, X = map(int, input().split())

C = []      # 値段を入れる配列
A = []      # 学びたいアルゴリズムを入れる配列


# それぞれの配列に値を入れる処理

for i in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])

ans = 10 ** 15                              # 最小値にバカでかい数を入れておく

for i in range(1 << N):                     # 「 1 << N 」 は 1 を左に N個 シフトする。例えば N = 8 の場合、 1 -> 100000000 となり、256 となる。
    cost = 0                                # これを for文 で使うと 0 ~ 255 になる。つまり、 0000000 ~ 1111111 となる。
    skill = [0] * M

    for shift in range(N):                  # N回 右にシフトしていく
        if i >> shift & 1 == 1:             # i を右にシフトした時に 1 と アンド演算を行い、1 となったら cost に値段を足していく
            cost += C[shift]

            for j in range(M):
                skill[j] += A[shift][j]
    
    if X <= min(skill):
        ans = min(ans, cost)

if ans == 10 ** 15:
    print(-1)

else:
    print(ans)