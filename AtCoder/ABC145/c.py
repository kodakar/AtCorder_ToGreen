from itertools import permutations
from math import sqrt

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

dist = 0
numbers = [i for i in range(N)]
all_c = list(permutations(numbers))

for c in all_c:
    for i in range(1, N):
        dist += sqrt((xy[c[i-1]][0] - xy[c[i]][0])**2 + (xy[c[i-1]][1] - xy[c[i]][1])**2)

print(dist/len(all_c))