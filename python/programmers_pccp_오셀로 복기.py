from collections import deque

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def move(s_x, s_y, index, visited):

    que = deque()
    que.append((s_x,s_y,1))
    while que:
        x, y, cnt = que.popleft()

        nx = x + dx[index]
        ny = y + dy[index]

        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue

        if board[nx][ny] == 'B' and not visited[nx][ny]:
            visited[nx][ny] = 1
            que.append((nx, ny, cnt+1))
        elif board[nx][ny] == 'W' and not visited[nx][ny]:
            return cnt

    return 0


def bfs(start_x, start_y, answer):
    visited = [[0] * 8 for _ in range(8)]
    total = 0

    que = deque()
    que.append((start_x, start_y, 0))

    while que:
        x, y, cnt = que.popleft()
        for index, i in enumerate([0,1,2,3,4,5,6,7,8]):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                continue

            if board[nx][ny] == 'B' and not visited[nx][ny]:
                visited[nx][ny] = 1
                total += move(nx, ny, index, visited)

    answer[start_x][start_y] = total


answer = [[0] * 8 for _ in range(8)]
board = ["........", "..B.W...", "..B.BBW.", "..BBBBW.", "...WBW..", "..W.....", "........", "........"]
for i in range(8):
    for j in range(8):
        if board[i][j] == '.':
            bfs(i, j, answer)

for i in answer:
    print(*i)


