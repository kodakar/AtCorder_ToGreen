# N = int(input())
# A = [0]
# A += list(map(int, input().split()))

# # d = [False] * (N + 1)

# def dfs(start, num):
#     next = A[num]
#     if d[next] == False:
#         a.append(next)
#         d[next] = True
#         if start == next:
#             print(len(a))
#             print(*a)
#             exit()
#         dfs(start, next)

# for i in range(1,N):
#     d = [False] * (N + 1)
#     a = []
#     dfs(i, i)

def find_cycle(graph, start):
    stack = [start]
    visited = set()

    while stack:
        current = stack[-1]

        if current in visited:
            return stack[stack.index(current):]

        visited.add(current)

        if graph[current] is not None:
            stack.extend(graph[current])

    return None


N = int(input())
A = list(map(int, input().split()))

graph = {i+1: [A[i]] for i in range(N)}

for i in range(1, N + 1):
    cycle = find_cycle(graph, i)
    if cycle:
        M = len(cycle)
        print(M-1)
        print(*cycle[1:])
        exit()
