n = int(input())

ans = 0

def judge_ten(n):
    a = str(n)

    if '7' in a:
        return True
    else:
        return False
    
def judge_eight(n):
    s = ""
    while n > 0:
        s = str(n % 8) + s
        n //= 8
    
    if '7' in s:
        return True
    else:
        return False

for i in range(1, n + 1):
    if judge_ten(i) == False and judge_eight(i) == False:
        ans += 1

print(ans)
    
#10進数をN進数にかえる方法
def Ten_to_N(n, N):
    s = ""
    while n > 0:
        s = str(n % N) + s  # 1 : nをNで割ったあまりを先頭に持ってくる
        n //= N             # 2 : nをNで割った商に置き換える
                            # これをnが0になるまで繰り返す
    print(s)