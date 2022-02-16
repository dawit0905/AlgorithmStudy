import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
cnt = 0
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(graph, start, visited):
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1, n + 1):
    if visited[i] == 0:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)
