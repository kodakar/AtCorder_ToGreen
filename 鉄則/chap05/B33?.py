N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

XOR = 0

for i in range(N):
    XOR = XOR ^ (AB[i][0] - 1)
    XOR = XOR ^ (AB[i][1] - 1)

print("Second" if XOR == 0 else "First")