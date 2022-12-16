import sys
import copy

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


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
parent2 = [i for i in range(n+1)]

edges = []
for i in range(m+1):
    v, w, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, v, w))

edges2 = copy.deepcopy(edges)
edges.sort(reverse=True)
edges2.sort()

# 최적의 코스
k = 0
for cost, v, w in edges:
    if find(parent, v) != find(parent, w):
        union(parent, v, w)
        if cost == 0:
            k += 1

# 최악의 코스
k2 = 0
for cost, v, w in edges2:
    if find(parent2, v) != find(parent2, w):
        union(parent2, v, w)
        if cost == 0:
            k2 += 1

print(k2**2 - k**2)


