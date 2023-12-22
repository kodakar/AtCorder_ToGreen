N = int(input())
S = [input() for _ in range(N)]

dict = {"AC":0, "WA":0, "TLE":0, "RE":0}

for i in S:
    dict[i] += 1

for i in dict:
    print(i,"x",dict[i])