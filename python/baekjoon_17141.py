import sys
from collections import deque
from collections import defaultdict
from itertools import combinations


def bfs(combi):
    que = deque()
    # -1:초기값, 0:바이러스 시작 위치, 1,2,3,4,5 ... 은 바이러스의 증가값들
    visited = [[-1] * n for _ in range(n)]
    for c in combi:
        x = c[0]
        y = c[1]
        que.append((x,y,0))
        visited[x][y] = 0

    while que:
        x, y, cost = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and (graph[nx][ny] == 0 or graph[nx][ny] == 2):
                    que.append((nx, ny, cost+1))
                    visited[nx][ny] = cost+1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and visited[i][j] == -1:
                return

    result = 0

    for i in range(n):
        result = max(result, max(visited[i]))

    return result


dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m = map(int, sys.stdin.readline().split())
# 0:빈칸, 1:벽, 2:바이러스
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

bias_index = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            bias_index.append((i, j))

combis = list(combinations(bias_index, m))

answer = sys.maxsize
for combi in combis:
    return_num = bfs(combi)
    if return_num != None:
        answer = min(answer, bfs(combi))

print(-1) if answer == sys.maxsize else print(answer)