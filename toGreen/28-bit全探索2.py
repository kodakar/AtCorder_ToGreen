H, W, K = map(int, input().split()) 

c = [list(input()) for _ in range(H)]

ans = 0

for row_red in range(1 << H):                # 1 を H 左シフトする。 H = 6 であれば 1000000　となって 範囲は 0 ~ 111111 
    for col_red in range(1 << W):            # 上と同様。 これで x行y列 が赤になっているかを2進数で表せる。 
        black = 0                            # row_red = 000001, col_red = 000100 であれば 1行3列 を塗っていることになる。

        for row in range(H):
            for col in range(W):
                
                if row_red >> row & 1 == 0 and col_red >> col & 1 == 0:     # それぞれを右にシフトして どちらも 1 でないのであれば黒を探す。
                    if c[row][col] == "#":
                        black += 1
        
        if black == K:
            ans += 1

print(ans)