N = int(input())

matrix = [0] * N

for i in range(N):
    matrix[i] = list(map(int, input().split(' ')))

begin_end = list(map(int, input().split(' ')))

visited = [-1] * N
visited[begin_end[0]] = 0

def bfs(graph, visited, end, now = 0, parent = -1):
    for neig in range(N):
        if neig != parent and graph[now][neig] == 1:
            visited[neig] = visited[now] + 1
            bfs(graph, visited, neig, now)
        if neig == end - 1:
            return visited[now] + 1

print(bfs(matrix, visited, begin_end[1], begin_end[0]))