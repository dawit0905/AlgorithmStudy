import sys


def dfs(k, temp, r, c):
    global n, m
    global answer

    steps = [(1 ,0), (0, 1), (-1, 0), (0, -1)]

    if k == 4:
        answer = max(answer, temp)
        return

    if temp + (4 - k) * max_val < answer:
        return

    for step in steps:
        next_r = r + step[0]
        next_c = c + step[1]
        if 0 <= next_r < n and 0 <= next_c < m:
            if visited[next_r][next_c] == 0:
                visited[next_r][next_c] = 1
                # ㅗ 표현
                if k == 2:
                    dfs(k+1, temp+arr[next_r][next_c], r, c)
                dfs(k+1, temp+arr[next_r][next_c], next_r, next_c)
                visited[next_r][next_c] = 0


n, m = map(int, sys.stdin.readline().split())
arr = []
answer = 0
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

max_val = max(map(max, arr))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(1, arr[i][j], i, j)
        visited[i][j] = 0

print(answer)