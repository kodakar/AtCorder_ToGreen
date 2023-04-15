n, k = map(int, input().split())

friends = [list( map(int, input().split())) for _ in range(n)]
friends.sort()

now_village = k

for i in range(n):
    f_village = friends[i][0]
    f_money = friends[i][1]

    if f_village <= now_village:
        now_village += f_money
    else:
        break

print(now_village)