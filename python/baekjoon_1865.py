import sys


def bf(start):
    distance[start] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            for next_node, cost in edges[j]:
                if distance[next_node] > distance[j] + cost:
                    distance[next_node] = distance[j] + cost
                    if i == n-1:
                        return True

    return False


t = int(sys.stdin.readline())
for _ in range(t):
    INF = sys.maxsize
    n, m, k = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n + 1)]
    distance = [INF] * (n+1)
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())

        edges[s].append((e, t))
        edges[e].append((s, t))
    for _ in range(k):
        s, e, t = map(int, sys.stdin.readline().split())
        edges[s].append((e, -t))

    negative_cycle = bf(1)

    if negative_cycle:
        print('YES')
    else:
        print('NO')
