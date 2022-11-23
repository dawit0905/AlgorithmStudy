# import sys
# import heapq
#
#
# def prim(start):
#     visited[start] = 1
#     que = graph[start]
#     heapq.heapify(que)
#     mst = []
#     total_weight = 0
#
#     while que:
#         weight, u, v = heapq.heappop(que)
#         if not visited[v]:
#             visited[v] = 1
#             mst.append((u, v))
#             total_weight += weight
#
#             for edge in graph[v]:
#                 if not visited[edge[2]]:
#                     heapq.heappush(que, edge)
#
#     return total_weight
#
#
# n = int(sys.stdin.readline())
# visited = [0] * (n+1)
# graph = [[] for _ in range(n+1)]
# for i in range(1, n+1):
#     tmp = list(map(int, sys.stdin.readline().split()))
#     for j in range(len(tmp)):
#         idx = j+1
#         if i != idx:
#             graph[i].append((tmp[j], i, idx))
#             graph[idx].append((tmp[j], idx, i))
#
# print(prim(1))


import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp


n = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
edges = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if i != j:
            edges.append((tmp[j], i, j))

edges.sort()

cnt = 0
answer = 0
for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        answer += weight
        cnt += 1
    if cnt == n-1:
        break

print(answer)
