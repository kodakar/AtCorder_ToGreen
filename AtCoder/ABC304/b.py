N = int(input())

if 10**3 <= N <= 10**4 - 1:
    N = str(N)
    N = int(N[0:len(N) - 1] + "0")

elif 10**4 <= N <= 10**5 - 1:
    N = str(N)
    N = int(N[0:len(N) - 2] + "00")

elif 10**5 <= N <= 10**6 - 1:
    N = str(N)
    N = int(N[0:len(N) - 3] + "000")

elif 10**6 <= N <= 10**7 - 1:
    N = str(N)
    N = int(N[0:len(N) - 4] + "0000")

elif 10**7 <= N <= 10**8 - 1:
    N = str(N)
    N = int(N[0:len(N) - 5] + "00000")

elif 10**8 <= N <= 10**9 - 1:
    N = str(N)
    N = int(N[0:len(N) - 6] + "000000")

print(N)