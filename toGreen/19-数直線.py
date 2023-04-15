
#  xは最初の座標、kは動く回数、dは動く量

x, k, d = map(int, input().split())

x = abs(x)

if 0 < x - k * d:
    print(abs(x - k * d))
else:
    move_count = k - x//d #　0になる直前に来た時の残り回数
    jump_before = x - d * (x//d) # 0になる直前の座標
    jump_after = jump_before - d # 0を超えた後の座標

    if move_count % 2 == 0:
        print(abs(jump_before))
    else:
        print(abs(jump_after))
