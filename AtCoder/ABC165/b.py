X = int(input())
now = 100
year = 0
while now < X:
    year += 1
    now += now//100
print(year)