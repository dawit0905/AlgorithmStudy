import sys
import copy


def dfs(graph, cnt):
    global answer

    if cnt == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += graph[i].count(0)
        answer = min(answer, cnt)
        return

    arr = copy.deepcopy(graph)

    cctv_num, x, y = cctv[cnt]
    for i in directions[cctv_num]:
        fill(arr, i, x, y)
        dfs(arr, cnt+1)
        arr = copy.deepcopy(graph)


def fill(temp, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if temp[nx][ny] == 6:
                break
            if temp[nx][ny] == 0:
                temp[nx][ny] = 7


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append([graph[i][j], i, j])

directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = sys.maxsize
dfs(graph, 0)
print(answer)
