import math
from collections import deque

def is_infected(N, coordinates, D):
    infected = [False] * N  # 各人の感染状態を管理するリスト
    infected[0] = True  # 人1を感染させる

    queue = deque([0])  # 探索対象のキュー
    while queue:
        current_person = queue.popleft()
        x1, y1 = coordinates[current_person]  # 探索中の人の座標
        for i in range(N):
            if not infected[i]:
                x2, y2 = coordinates[i]  # 感染していない人の座標
                distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # ユークリッド距離の計算
                if distance <= D:
                    infected[i] = True
                    queue.append(i)

    return infected

# 入力を受け取る
N, D = map(int, input().split())  # 人の数
coordinates = []  # 各人の座標を格納するリスト
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# ウイルス感染の判定
infected_status = is_infected(N, coordinates, D)

# 結果を出力
for status in infected_status:
    if status:
        print("Yes")
    else:
        print("No")

