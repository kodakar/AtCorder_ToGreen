import itertools

n, k = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for root in itertools.permutations(range(1, n - 1)):
    now_time = 0
    now_time += time[0][root[0]]
    
    now_city = root[0]

    for i in range(1, n - 1):
        to_city = root[i]
        now_time += time[now_city][to_city]
        now_city = to_city

    now_time += time[now_city][0]
    if now_time == k:
        ans += 1

print(ans)

import itertools
# 順列
#(1,2,3),(1,3,2),(2,1,3),(2,3,1),...,(3,2,1)
for seq in itertools.permutations(range(1,4)):
    pass
# 重複なしの組み合わせ
# (1,2,3),(1,2,4),...,(7,8,9)
for seq in itertools.combinations(range(1,10),3):
    pass
# 重複ありの組み合わせ
#(1,1,1),(1,1,2),...,(9,9,9)
for seq in itertools.combinations_with_replacement(range(1,10),3):
    pass
# 直積
#(1,1),(1,2),(1,3),(2,1),(2,2),...,(3,3)
for seq in itertools.product(range(1,4),range(1,4)):
    pass