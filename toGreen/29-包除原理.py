N = int(input())

mod = 10 ** 9 + 7

A_all = pow(10, N, mod)             # 数列全体の数
A_0 = pow(9, N, mod)                # 0を含まない数列の数
A_9 = pow(9, N, mod)                # 9を含まない数列の数
A_0_9 = pow(8, N, mod)              # 0も9も含まない数列の数

ans = A_all - ( A_0 + A_9 - A_0_9)  # 数列全体の数から 0 または 9 を含まない数列の数を引いて 0 と 9 を含む数列の数を求める
ans %= mod

print(ans)