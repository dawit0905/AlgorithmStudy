import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)
graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
