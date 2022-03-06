import sys

sys.setrecursionlimit(10**9)

def dfs(graph, visited, node):
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            answer[i] = node
            dfs(graph, visited, i)


n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
answer = [0] * (n+1)
visited = [0] * (n+1)


for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, visited, 1)

for i in answer[2:]:
    print(i)
