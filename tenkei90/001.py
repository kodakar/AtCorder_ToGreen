# 二分探索（最小値の最大を求めるときは二分探索）

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(x):
    num = 0                     # 何個に切れたか
    pre = 0                     # 切ったとこの場所
    for i in range(N):
        if A[i] - pre >= x:     # 切れ目の位置が mid より大きいかどうか
            num += 1            # 大きかったら切る
            pre = A[i]          # 切った場所を保存

    if L - pre >= x:            # 余った部分も確認
        num += 1                

    if num >= K + 1:            # 切れ目の数が K+1 より大きいかどうか
        return True
    else:
        return False
    
ok = -1                         # 左端
ng = L + 1                      # 右端

while(abs(ok - ng) > 1):        # 左端と右端の隙間が無くなったら終わり
    mid = (ok + ng) //2         # 中央値
    if check(mid):              # mid 以上のようかんが K+1 に切れるかチェック
        ok = mid                # 切れるなら中央値を右側に代入
    else:
        ng = mid                # 切れないなら中央値を左側に代入

print(ok)