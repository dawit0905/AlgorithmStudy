import sys
from collections import deque


# 영역 숫자 매기기
def fill_number(x, y, num):
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    graph[x][y] = num

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and\
                    not visited[nx][ny] and graph[nx][ny] != 0:
                graph[nx][ny] = num
                visited[nx][ny] = 1
                que.append((nx, ny))

# 다리를 bfs로 탐색하면서 크루스칼에 사용할
# edges(cost, v, w) 찾기
def make_bridge(x, y):
    que = deque()
    que.append((x, y))
    my_num = graph[x][y]

    while que:
        x, y = que.popleft()

        for i in range(4):
            cost = 0
            nx = x
            ny = y
            while True:
                nx = nx + dx[i]
                ny = ny + dy[i]
                cost += 1

                # 전체 범위를 초과하는 경우
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break

                # 다음값이 내 땅인 경우
                if graph[nx][ny] == my_num:
                    break


                # 다음 값이 0이 아닌경우
                if graph[nx][ny] != 0:
                    # 다음 값이 내땅이 아닌데, cost가 2보다 작거나 같은경우.
                    if graph[nx][ny] != my_num and cost <= 2:
                        break
                    edges.append(
                        (cost-1, my_num, graph[nx][ny]))
                    break


def find(parent, x):
    if parent[x] != x:
        parent[x] = (find(parent, parent[x]))

    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[0] * m for _ in range(n)]

num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            num += 1
            fill_number(i, j, num)


# cost, v, w, nx, ny
edges = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            make_bridge(i, j)

edges.sort()
parent = [i for i in range(num+1)]
answer = 0
cnt = 0
for cost, v, w in edges:
    if find(parent, v) != find(parent, w):
        union(parent, v, w)
        answer += cost
        cnt += 1


if cnt == num-1:
    print(answer)
else:
    print(-1)

