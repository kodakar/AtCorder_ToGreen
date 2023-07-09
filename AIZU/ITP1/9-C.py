n = int(input())
cards = [input().split() for _ in range(n)]
cards_copy = cards.copy()

taro = 0
hanako = 0
for i in range(len(cards)):
    if cards[i][0] == cards[i][1]:
        taro += 1
        hanako += 1
    elif cards_copy[i] == sorted(cards[i]):
        hanako += 3
    else:
        taro += 3

print(taro, hanako)