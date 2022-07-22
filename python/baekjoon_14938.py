import sys
import heapq


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for next_node, cost in edges[now]:
            next_cost = dist + cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(que, (next_cost, next_node))

    return distance


n, m, r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))
edges = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

answer = 0
for i in range(1, n+1):
    arr = dijkstra(i)
    temp = 0
    for j in range(1, n+1):
        if arr[j] <= m:
            temp += item[j]
    answer = max(answer, temp)

print(answer)
