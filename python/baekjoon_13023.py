import sys


def dfs(node, depth):
    if depth == 4:
        print(1)
        exit()

    for i in arr[node]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth+1)
            visited[i] = 0


n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n)]
visited = [0] * n

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


# 노드를 순서대로 방문하며 dfs를 수행합니다.
for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(0)
