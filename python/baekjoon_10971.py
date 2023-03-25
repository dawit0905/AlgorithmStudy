import sys


def dfs(now, c):
    global MAX
    if c < MAX:
        if all(visited) and now == 0:
            MAX = min(MAX, c)

        for i in range(n):
            if edges[now][i] > 0 and not visited[i]:
                visited[i] += 1
                dfs(i, c+edges[now][i])
                visited[i] -= 1


n = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visited = [0] * n
MAX = sys.maxsize

dfs(0, 0)
print(MAX)

