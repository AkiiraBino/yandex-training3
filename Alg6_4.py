from sys import setrecursionlimit

setrecursionlimit(40000)
value = []
def dfs(graph, visited, now = 1):
    if visited[now] != 2:
        visited[now] = 1
        for neig in graph[now]:
            if visited[neig] == 0:
                if dfs(graph, visited, neig) == 0:
                    return 0
                if neig not in value:
                    value.append(neig)
            elif visited[neig] == 1:
                return 0
            visited[neig] = 2

        if now not in value:
            value.append(now)
        visited[now] = 2
        return 1
    elif visited[now] == 1:
        return 0
    else:
        return 1

def main():

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
        if value[1] not in graph[value[0]]:
            graph[value[0]].append(value[1])



    visited = [0] * (NM[0] + 1)

    for i in range(1, NM[0] + 1):
        if not dfs(graph, visited, i):
            return 0
    return 1



if __name__ == "__main__":
    if main():
        value = list(map(str, value))
        print(' '.join(value[::-1]))
    else:
        print(-1)