import sys


def dfs(node):
    global n

    for next in range(n):
        if graph[node][next] == 'Y':
            visited[node][next] = 1
            for j in range(n):
                if graph[next][j] == 'Y' and node != j:
                    visited[node][j] = 1


n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    dfs(i)

answer = 0
for i in range(n):
    answer = max(answer, sum(visited[i]))

print(answer)
