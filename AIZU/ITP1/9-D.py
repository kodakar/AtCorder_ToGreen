s = input()
q = int(input())
for i in range(q):
    o = list(input().split())
    a, b = int(o[1]), int(o[2])
    if o[0] == "replace":
        s = s[:a] + o[3] + s[b+1:]
    elif o[0] == "reverse":
        tmp = s[a:b+1]
        s = s[:a] + tmp[::-1] + s[b+1:]
    else:
        print(s[a:b+1])