S = input()
t = ""                      # 現在の文字列
count = 0                   # 区切りのカウント
prev = ""                   # 一個前の文字列

for i in range(len(S)):
    t += S[i]               # t に S を付ける  prev が t と等しい時はどんどん付けていく

    if prev != t:           # もし前の文字列の t が一緒じゃなかったら
        count += 1          # 区切る
        prev = t            # 前の文字列を t にする
        t = ''              # t を initialize

print(count)
