import sys
from collections import deque
from itertools import combinations


def bfs(combi, leftArea):
    global wall_cnt
    que = deque()
    # -1:초기값, 0:바이러스 시작 위치, 1,2,3,4,5 ... 은 바이러스의 증가값들
    visited = [[-1] * n for _ in range(n)]
    for c in combi:
        x = c[0]
        y = c[1]
        que.append((x,y,0))
        visited[x][y] = 0

    result = 0
    while que:
        if not leftArea:
            break

        x, y, cost = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않았고, 빈칸일때
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    que.append((nx, ny, cost+1))
                    visited[nx][ny] = cost+1
                    result = max(result, visited[nx][ny])
                # 방문하지 않았고,
                elif visited[nx][ny] == -1 and graph[nx][ny] == 2:
                    que.append((nx, ny, cost+1))
                    visited[nx][ny] = cost+1

    if not leftArea:
        return result

    if list(sum(visited, [])).count(-1) != wall_cnt:
        return sys.maxsize
    return result


dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m = map(int, sys.stdin.readline().split())
# 0:빈칸, 1:벽, 2:바이러스
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

bias_index = []
bias_cnt = 0
wall_cnt = 0
left = 0
for i in range(n):
    for j in range(n):

        if graph[i][j] == 0:
            left += 1

        elif graph[i][j] == 1:
            wall_cnt += 1

        elif graph[i][j] == 2:
            bias_index.append((i, j))
            bias_cnt += 1



combis = list(combinations(bias_index, m))

answer = sys.maxsize
for combi in combis:
    answer = min(answer, bfs(combi, left))

print(-1) if answer == sys.maxsize else print(answer)

