import sys
sys.setrecursionlimit(4000)


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
    if value[0] not in graph[value[1]] and value[0] != value[1]:
        graph[value[0]].append(value[1])
        graph[value[1]].append(value[0])
    

visited = [False] * (NM[0] + 1)
color = [0] * (NM[0] + 1)
curr_color = 2
value = []


def dfs(graph, visited, color, curr_color, now = 1):
    visited[now] = True
    color[now] = curr_color
    for neig in graph[now]:
        if not visited[neig]:
            value.append(dfs(graph, visited, color,3 - curr_color, neig))
        if color[neig] == color[now]:
            return 0
    return 1

count = 0
for i in range(1, NM[0] + 1):
    if not visited[i]:
        value.append(dfs(graph, visited, color, 3 - curr_color, now=i))
    if (not value[-1]) or (0 in value):
        print("NO")
        break
    else:
        count+=1

if count == len(value) and 0 not in value:
    print("YES")