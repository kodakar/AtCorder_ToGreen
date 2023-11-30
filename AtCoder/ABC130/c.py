W, H, x, y = map(int, input().split())

a = (W * H)/2
c = int(x == W/2 and y==H/2) # x, y が長方形の中心だと複数引ける
print(a,c)