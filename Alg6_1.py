import sys
sys.setrecursionlimit(4000)
def dfs(graph, visited, now = 1, count = 0):

    visited[now] = True
    count+=1
    for neig in graph[now]:
        if not visited[neig]:
            count = dfs(graph, visited, neig, count)
    result[-1].append(str(now))
    return count

values = 0

with open("input.txt") as file:
    values = file.readlines()
    values = [i.rstrip() for i in values]

NM = list(map(int, values[0].split(' ')))
graph = [0] * (NM[0] + 1)
for i in range(1, NM[0] + 1):
    graph[i] = []

for i in range(1, NM[1] + 1):
    value = list(map(int, values[i].split(' ')))
    if value[0] not in graph[value[1]]:
        graph[value[0]].append(value[1])
        graph[value[1]].append(value[0])
    

visited = [False] * (NM[0] + 1)
count_adj = 0
count = []
result = []


for i in range(1, NM[0] + 1):

    if not visited[i]:
        count_adj += 1
        result.append([])
        count.append(dfs(graph, visited, now=i))


print(count_adj)
for i in range(count_adj):
    print(count[i])
    print(' '.join(result[i]))