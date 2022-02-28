import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())
graph = [[inf] * (n+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0


for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

arr = []
for i in range(0,n+1):
    arr.append(sum(graph[i][1:]))

print(arr.index(min(arr)))
