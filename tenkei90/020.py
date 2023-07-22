a, b, c = map(int, input().split())

if a < c**b:
    print("Yes")
else:
    print("No")


# ex) log(a) と b×log(c) の大小関係 → a ,c^bの大小関係と等しくなる。