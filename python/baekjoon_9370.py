import sys
import heapq


def dijkstra(start):
    global n
    que = []
    que.append((0, start))
    distance = [INF] * (n+1)
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            next_cost = dist + cost
            if next_cost < distance[node]:
                distance[node] = next_cost
                heapq.heappush(que, (next_cost, node))

    return distance

INF = int(1e9)
tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    destination_candidate = []
    for i in range(t):
        destination_candidate.append(int(sys.stdin.readline()))

    s_list = dijkstra(s)
    g_list = dijkstra(g)
    h_list = dijkstra(h)


    answer = []
    for i in destination_candidate:
        #
        if s_list[g] + g_list[h] + h_list[i] == s_list[i] or s_list[h] + g_list[i] + h_list[g] == s_list[i]:
            answer.append(i)

    answer.sort()
    print(*answer)

