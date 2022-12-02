import sys


def dfs(now, depth):
    if depth == 2:
        return
    for next in graph[now]:
        if not visited[next]:
            visited[next] = 1
        dfs(next, depth+1)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[1] = 1

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
print(visited.count(1)-1)