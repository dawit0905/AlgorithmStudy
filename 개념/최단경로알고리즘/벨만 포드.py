import sys


# 벨만-포드 baekjoon_11657과 같음
def bf(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost

                if i == n - 1:
                    return True
    return False


n, m = map(int, sys.stdin.readline().split())
INF = sys.maxsize
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])



