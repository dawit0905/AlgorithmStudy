import sys

n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])
