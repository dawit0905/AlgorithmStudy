import sys
import heapq


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while(que):
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, (cost, next_node))


INF = int(1e9)
t = int(sys.stdin.readline())
for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n+1)

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))

    dijkstra(c)

    cnt = 0
    answer = 0
    for i in range(1, n+1):
        if distance[i] == INF:
            continue
        else:
            cnt += 1
            answer = max(answer, distance[i])
    print(cnt, answer)
