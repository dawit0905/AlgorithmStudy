import sys


def dfs(x, y, flag):
    global answer

    if x == n-1 and y == n-1:
        answer += 1
        return

    if flag == 0 or flag == 2:
        if y+1 < n:
            if graph[x][y+1] == 0:
                dfs(x, y+1, 0)
    if flag == 1 or flag == 2:
        if x+1 < n:
            if graph[x+1][y] == 0:
                dfs(x+1, y, 1)

    if x+1 < n and y+1 < n:
        if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)


n = int(sys.stdin.readline())
graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dfs(0, 1, 0)
print(answer)
