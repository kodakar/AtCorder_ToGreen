B = int(input())

for i in range(1,16):
    if i**i == B:
        print(i)
        exit()

print(-1)