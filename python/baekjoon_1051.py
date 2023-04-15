import sys


n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

nums = [[] for _ in range(10)]

for i in range(n):
    for j in range(m):
        num = graph[i][j]

        nums[num].append([i, j])

answer = 1
for i in range(10):
    for x, y in nums[i]:
        nx = x
        ny = y
        j = 1
        while True:
            nx += 1
            ny += 1

            if nx >= n or ny >= m or j >= n or j >= m:
                break

            if graph[x][y] == graph[x][ny] and graph[x][y] == graph[nx][y] and graph[x][y] == graph[nx][ny]:
                answer = max(answer, (j+1)**2)

            j += 1

print(answer)