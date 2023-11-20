# --------------- 通常 ----------------

# N = int(input())

# def prime_check(x):
#     for i in range(2, int(x**(1/2))+1):
#         if x % i == 0:
#             return False
#     return True

# for i in range(2,N+1):
#     if prime_check(i):
#         print(i)


# ------------ エラストテネス -----------

N = int(input())
d = [False for _ in range(N+1)]

for i in range(2, int(N**(1/2))+1):
    if d[i] == False:
        for j in range(i*2, N + 1, i):
                d[j] = True

for i in range(2, N+1):
     if d[i] == False:
          print(i)

