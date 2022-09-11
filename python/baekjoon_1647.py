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


n, m = map(int, sys.stdin.readline().split())
edge = []
parent = [i for i in range(n+1)]
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edge.append((cost, a, b))

edge.sort()

result = 0
last_house_cost = 0
for cost, a, b in edge:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        last_house_cost = cost

print(result - last_house_cost)