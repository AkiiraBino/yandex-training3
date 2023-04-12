N = int(input())

matrix = [0] * N

for i in range(N):
    matrix[i] = list(map(int, input().split(' ')))

visited = [0] * N

V = []

def dfs(graph, visited,  now = 0, parent = 0):
    visited[now] = 1

    for neig in range(N):
        if graph[now][neig] == 1 and visited[neig] == 0:
            if dfs(graph, visited, neig, now):
                V.append(now)
                return 1
        elif graph[now][neig] == 1 and visited[neig] == 1 and neig != parent:
            V.append(now)
            return 1
    visited[now] = 2
    return 0

for i in range(N):
    if visited[i] == 0:
        dfs(matrix, visited, i)
    if V != []:
        break

if V != []:
    print("YES")
    print(len(V))
    print(' '.join([str(i + 1) for i in V]))
else:
    print("NO")