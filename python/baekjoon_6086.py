import sys
from collections import deque


def ctoi(c):
    if c.isupper():
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26


def bfs(source, destination, visited):
    que = deque()
    que.append(source)

    while que and visited[destination] == -1:
        sv = que.popleft()

        for dv in adjList[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visited[dv] == -1:
                que.append(dv)
                visited[dv] = sv

                if dv == destination:
                    break

    if visited[destination] == -1:
        return True
    else:
        return False


def edmondKarp(source, destination):
    totalFlow = 0

    while 1:
        visited = [-1] * MAXV
        if bfs(source, destination, visited):
            break

        minFlow = sys.maxsize
        i = destination

        while i != source:
            minFlow = min(minFlow, capacity[visited[i]][i] - flow[visited[i]][i])
            i = visited[i]

        i = destination
        while i != source:
            flow[visited[i]][i] += minFlow
            flow[i][visited[i]] -= minFlow
            i = visited[i]

        totalFlow += minFlow

    return totalFlow


sys.setrecursionlimit(int(10**7))
n = int(sys.stdin.readline())
MAXV = 52
capacity = [[0] * MAXV for _ in range(MAXV)]
flow = [[0] * MAXV for _ in range(MAXV)]
adjList = [[] for _ in range(MAXV)]

for i in range(n):
    source, destination, cost = map(str, sys.stdin.readline().split())

    source = ctoi(source)
    destination = ctoi(destination)

    capacity[source][destination] += int(cost)
    capacity[destination][source] += int(cost)
    adjList[source].append(destination)
    adjList[destination].append(source)

source = ctoi('A')
destination = ctoi('Z')


print(edmondKarp(source, destination))
