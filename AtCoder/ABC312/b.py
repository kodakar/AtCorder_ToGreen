N, M = map(int, input().split())

S = [list(input()) for _ in range(N)]

# print(S)

for c in range(N):
    for r in range(M):
        if S[c][r] == "#" and c + 8 < N and r + 8 < M:
            # if 0 < r:
            #     if S[c][r-1] == "#":
            #         continue
            #     if S[c+1][r-1] == "#":
            #         continue
            #     if S[c+2][r-1] == "#":
            #         continue
            # if 0 < c:
            #     if S[c-1][r:r+4] != [".",".",".","."]:
            #         continue
            
            # if 0 < c and 0 < r:
            #     if S[c-1][r-1] == "#":
            #         continue

            # if r + 9 < M:
            #     if S[c+5][r+9] == "#":
            #         continue
            #     if S[c+6][r+9] == "#":
            #         continue
            #     if S[c+7][r+9] == "#":
            #         continue
            #     if S[c+8][r+9] == "#":
            #         continue

            # if c + 9 < N:
            #     if S[c+9][r+5:r+9] != [".",".",".","."]:
            #         continue

            # if c + 9 < N and r + 9 < M:
            #     if S[c+9][r+9] == "#":
            #         continue
                    

            if S[c][r:r+4] != ["#","#","#","."]:
                continue
            if S[c+1][r:r+4] != ["#","#","#","."]:
                continue
            if S[c+2][r:r+4] != ["#","#","#","."]:
                continue  
            if S[c+3][r:r+4] != [".",".",".","."]:
                continue

            if S[c+5][r+5:r+9] != [".",".",".","."]:
                continue
            if S[c+6][r+5:r+9] != [".","#","#","#"]:
                continue
            if S[c+7][r+5:r+9] != [".","#","#","#"]:
                continue
            if S[c+8][r+5:r+9] != [".","#","#","#"]:
                continue

            print(c+1,r+1)