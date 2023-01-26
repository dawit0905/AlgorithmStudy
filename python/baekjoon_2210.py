import sys


def dfs(x, y, depth, pattern):
    global answer_list

    if depth == 6:
        if pattern not in answer_list:
            answer_list.append(pattern)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5 and len(pattern) != 6:
            pattern += str(graph[nx][ny])
            dfs(nx, ny, depth+1, pattern)
            pattern = pattern[:-1]


graph = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = 0
answer_list = []
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, '')


# print(answer_list)
print(len(answer_list))
