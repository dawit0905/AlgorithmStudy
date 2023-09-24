import sys


def dfs(x, y):
    if y == c-1:
        return True

    for dx in [-1,0,1]:
        nx = x + dx
        ny = y + 1

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != 'x' and not visited[nx][ny]:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True

    return False


r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
cnt = 0

for i in range(r):
    if dfs(i, 0):
        cnt += 1

print(cnt)