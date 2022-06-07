import sys
from collections import deque


n = int(sys.stdin.readline())
graph = []
distance = [[-1] * n for i in range(n)]
distance[0][0] = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

que = deque()
que.append((0, 0))


while que:
    x, y = que.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            if distance[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    que.appendleft((nx, ny))
                    distance[nx][ny] = distance[x][y]
                else:
                    que.append((nx, ny))
                    distance[nx][ny] = distance[x][y]+1

print(distance[n-1][n-1])
# for i in distance:
#     print(*i)