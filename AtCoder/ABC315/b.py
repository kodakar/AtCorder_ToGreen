M = int(input())
D = list(map(int, input().split()))

a = 0
new_D = [0]

for i in range(M):
    a += D[i]
    new_D.append(a)

middle = sum(D)/2
# print(new_D)
# print(middle)
for i in range(M):
    # print(new_D[i],middle,new_D[i+1])
    if new_D[i] < middle <= new_D[i+1]:
        print(i+1, int(D[i] - (new_D[i+1]-middle) + 1))
        exit()