from collections import deque

S = input()
Q = int(input()) 

inv = False

S_deque = deque()

for i in range(len(S)):
    S_deque.append(S[i])

for i in range(Q):
    TFC = list(map(str, input().split()))
    
    if TFC[0] == "1":
        if inv == True:
            inv = False
        else:
            inv = True

    elif TFC[0] == "2" :
        if inv == False:
            if TFC[1] == "1":
                S_deque.appendleft(TFC[2])
            else:
                S_deque.append(TFC[2])
        else:
            if TFC[1] == "1":
                S_deque.append(TFC[2])
            else:
                S_deque.appendleft(TFC[2])

ans = "".join(S_deque)

if inv == True:
    ans = ans[::-1]

print(ans)